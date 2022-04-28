#!/usr/bin/python

# (c) 2022, NetApp, Inc
# License: BSD-3-Clause
from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: netapp_eseries.host.update_conf
short_description: Update configuration file
description:
    - Update an existing configuration file with specified options.
author: Nathan Swartz (@ndswartz)
options:
    path:
        description:
            - Path to configuration file to be updated.
            - Hidden backup of the original configuration file will be made when I(backup_original==True)
            - I(path) is mutually exclusive with I(src) and I(dest).
        type: str
        required: false
    backup_original:
        description:
            - Whether to create a backup of the original configuration file when I(path) is provided.
            - When I(backup_original==False) and I(path) is specified then there will be no source for the original
              configuration defaults; so when an option is removed from I(options) it will remain the same rather than
              reverting to its original value.
            - No backup will be made when I(src) is provided.
            - I(insert_block_comments==True) option can be used in conjunction or as an alternative to backup_original.
        type: bool
        required: false
        default: true
    backup_path:
        description:
            - Path where the backup configuration file should be placed.
            - When I(backup_path) is specified then the original configuration file, I(path), will be used as part of
              the name to avoid conflicts with slashes replaced with underscores.
            - This is useful when all configuration files are read within the directory resulting in duplicate
              configuration files.
        type: str
        required: false
    backup_extension:
        description: String that will be postpended to the I(path) file name.
        type: str
        required: false
        default: ".~ansible-original"
    src:
        description:
            - Source for the base standard Linux conf file.
            - I(src) is mutually exclusive with I(path)
        type: str
        required: false
    dest:
        description:
            - Destination for the updated standard Linux conf file.
            - I(dest) is mutually exclusive with I(path)
        type: str
        required: false
    options:
        description: Dictionary containing the options key-value pairs to update conf file.
        type: dict
        required: false
        default: {}
    pattern:
        description:
            - Regular expression pattern to capture and update options
            - Must return three groups in the format "^(option)(equivalence)(value)$.
        type: str
        required: false
        default: "^#? ?([A-Za-z0-9._-]+)( *= *)(.*)$"
    padding:
        description: Ensures there's padding after the equivalence.
        type: bool
        require: false
    comment_start:
        description: Character that is used to indicate a line should be skipped or ignored.
        type: str
        required: false
        default: "#"
    mode:
        description:
            - The permissions the destination and backup configuration files should have.
            - The permissions must be in octal number form ("0644", "644"). Be sure to place these in quotes to avoid
              unintended integer conversion.
            - When not specified, the file permissions will be determined by the operating system defaults.
        type: str
        required: false
    block_message:
        description:
            - The message on the begin and end marker lines within the configuration file for options that were not
              found.
        type: str
        required: false
        default: ANSIBLE NETAPP_ESERIES.HOST.UPDATE_CONF MANAGED BLOCK
    insert_block_comments:
        description: Whether to wrap options that are undefined in the source configuration file within comment blocks.
        type: bool
        required: false
        default: true
    insert_pattern:
        description: String or regular expression that is used to determine the line to insert before or after.
        type: str
        required: false
    insert:
        description:
            - Where to insert options that are undefined in the source configuration file.
            - I(insert=="before") and I(insert=="after") requires I(insert_pattern) to be defined.
            - If I(insert=="skip") then any option that was undefined in the source configuration file will not be
              appended.
            - Warning is issued whenever option(s) are specified that are not defined in the source configuration file.
        type: str
        default: end
        choices:
            - beginning
            - end
            - before
            - after
            - skip
notes:
    - Configuration file with options that are not found will be placed at the end of the file within a comment block
      and a warning will be issued.
"""

RETURN = """
msg:
    description: Message describing what was changed.
    returned: on success
    type: str
    sample: Configuration file changed.
source:
    description: Source of the configuration file.
    returned: on success
    type: str
    sample: /etc/iscsi/iscsid.conf
backup:
    description: The original configuration file's backup that is used to maintain the original configuration.
    returned: on success
    type: str
    sample: /etc/iscsi/.iscsid.conf.~original
destination:
    description: Destination of the configuration file.
    returned: on success
    type: str
    sample: /etc/iscsi/iscsid.conf
"""

EXAMPLES = """
- name: Update iscsid.conf.
  netapp_eseries.host.update_conf:
    path: /etc/iscsi/iscsid.conf
    options:
      node.session.timeo.replacement_timeout: 20
      node.session.queue_depth: 128
      node.session.nr_sessions: 2
  become: true
"""

from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule
import re
from os.path import exists, isfile, abspath, basename, dirname
from os import chmod, stat

class UpdateConfigFile(object):
    def __init__(self):
        ansible_options = dict(
            path=dict(type="str", require=False),
            backup_original=dict(type="bool", require=False, default=True),
            backup_path=dict(type="str", required=False),
            backup_extension=dict(type="str", required=False, default=".~ansible-original"),
            src=dict(type="str", require=False),
            dest=dict(type="str", require=False),
            options=dict(type="dict", required=False, default={}),
            pattern=dict(type="str", required=False, default="^#? ?([A-Za-z0-9._-]+)( *= *)(.*)$"),
            padding=dict(type="bool", required=False, default=True),
            comment_start=dict(type="str", required=False, default="#"),
            mode=dict(type="str", required=False),
            block_message=dict(type="str", required=False,
                               default="ANSIBLE NETAPP_ESERIES.HOST.UPDATE_CONF MANAGED BLOCK"),
            insert_block_comments=dict(type="bool", required=False, default=True),
            insert_pattern=dict(type="str", required=False),
            insert=dict(type="str", required=False, choices=["beginning", "end", "before", "after", "skip"],
                        default="end")
        )
        self.module = AnsibleModule(argument_spec=ansible_options,
                                    required_one_of=[["path", "src"]],
                                    mutually_exclusive=[["path", "src"]],
                                    required_together=[["src", "dest"]],
                                    required_if=[["insert", "before", ["insert_pattern"]],
                                                 ["insert", "after", ["insert_pattern"]]],
                                    supports_check_mode=True)

        args = self.module.params
        if args["path"]:
            self.source = abspath(args["path"])
            self.destination = self.source
            if args["backup_original"]:
                if args["backup_path"]:
                    backup_filename = "." + re.sub("[\/]+", "_", self.source) + args["backup_extension"]
                    self.path_directory = args["backup_path"].rstrip("/")
                else:
                    backup_filename = "." + basename(self.source) + args["backup_extension"]
                    self.path_directory = dirname(self.source)
                self.backup_source = self.path_directory + "/" + backup_filename
            else:
                self.backup_source = None
        else:
            self.source = abspath(args["src"])
            self.destination = args["dest"]
            self.backup_source = None

        self.options = args["options"]
        self.pattern = args["pattern"]
        self.padding = args["padding"]
        self.comment_start = args["comment_start"]
        self.mode = args["mode"]
        self.block_message = args["block_message"]
        self.insert_block_comments = args["insert_block_comments"]
        self.insert_pattern = args["insert_pattern"]
        self.insert = args["insert"]

        self.copy_lines_cached = None
        self.update_configuration_file_required_cached = None
        self.update_mode_required_cached = None
        self.backup_original_source_required_cache = None

    @property
    def updated_copy(self):
        """Create a copy of the source configuration file in memory and update the options."""
        options = self.options.keys()
        options_applied = []

        if self.copy_lines_cached is None:
            comment_begin = "%s BEGIN %s\n" % (self.comment_start, self.block_message)
            comment_end = "%s END %s\n" % (self.comment_start, self.block_message)
            comment_block_begin_index = None
            comment_block_end_index = None
            insert_index = None

            source = self.backup_source or self.source
            with open(source, "r") as fh:
                self.copy_lines_cached = fh.readlines()

            # Update the copy with the options provided.
            comment_section = False
            for index, line in enumerate(self.copy_lines_cached):

                # Skip comment section to address any options that are not expected later.
                if line == comment_begin:
                    comment_section = True
                    comment_block_begin_index = index
                    continue
                elif line == comment_end:
                    comment_section = False
                    comment_block_end_index = index
                    continue
                elif comment_section:
                    continue

                result = re.search(self.pattern, line)
                if result:
                    option, equivalence, value = list(result.groups())
                    if option in options:
                        options_applied.append(option)
                        if self.padding:
                            self.copy_lines_cached[index] = "%s%s %s\n" % (option, equivalence.rstrip(" "),
                                                                           str(self.options.pop(option)))
                        else:
                            self.copy_lines_cached[index] = "%s%s%s\n" % (option, equivalence,
                                                                          str(self.options.pop(option)))

                    # Comment out any expected options that have already been set previously to prevent duplicates
                    elif not re.search("^%s" % self.comment_start, line) and option in options_applied:
                        self.copy_lines_cached[index] = "%s%s\n" % (self.comment_start, line)

            # Remove all options within existing comment block.
            if comment_block_begin_index is not None:
                for index in range(comment_block_begin_index, comment_block_end_index + 1):
                    self.copy_lines_cached.pop(comment_block_begin_index)

            # Check for whether any options were not used. If so, insert them into a comment block and issue a warning.
            if self.options:
                self.module.warn("Warning! Option(s) were not found and have been placed within a comment block at the"
                                 " end of the configuration file. Option(s) not found: [%s]" % ", ".join(self.options))

                if self.insert != "skip":

                    # Determine the index to insert remaining options.
                    if self.insert in ["before", "after"]:
                        for index, line in enumerate(self.copy_lines_cached):
                            if re.search(self.insert_pattern, line):
                                insert_index = index if self.insert == "before" else index + 1
                    elif self.insert == "beginning":
                        insert_index = 0
                    else:
                        insert_index = len(self.copy_lines_cached) + 1

                    # Add all remaining options
                    if self.insert_block_comments:
                        self.copy_lines_cached.insert(insert_index, comment_begin)
                        insert_index += 1

                    for option, value in self.options.items():
                        if self.padding:
                            self.copy_lines_cached.insert(insert_index, "%s = %s\n" % (option, value))
                        else:
                            self.copy_lines_cached.insert(insert_index, "%s=%s\n" % (option, value))
                        insert_index += 1

                    if self.insert_block_comments:
                        self.copy_lines_cached.insert(insert_index, comment_end)
                        insert_index += 1
        return self.copy_lines_cached

    @property
    def backup_original_source_required(self):
        """Check whether a copy of the source file needs to be created."""
        if self.backup_original_source_required_cache is None:
            self.backup_original_source_required_cache = False

            if self.backup_source is not None and not exists(self.backup_source):
                self.backup_original_source_required_cache = True

        return self.backup_original_source_required_cache

    @property
    def update_configuration_file_required(self):
        """Determine whether an update is required."""
        if self.update_configuration_file_required_cached is None:
            self.update_configuration_file_required_cached = False

            if exists(self.destination):
                with open(self.destination, "r") as fh:
                    self.update_configuration_file_required_cached = self.updated_copy != fh.readlines()
            else:
                self.update_configuration_file_required_cached = True

        return self.update_configuration_file_required_cached

    @property
    def update_mode_required(self):
        """Determine whether an update is required."""
        if self.update_mode_required_cached is None:
            self.update_mode_required_cached = False

            if self.mode:
                if exists(self.destination):
                    source_mode = oct(stat(self.destination).st_mode)[-1 * len(self.mode):]
                else:
                    source_mode = oct(stat(self.source).st_mode)[-1 * len(self.mode):]
                self.update_mode_required_cached = self.mode != source_mode

                if self.backup_source is not None and exists(self.backup_source):
                    backup_mode = oct(stat(self.backup_source).st_mode)[-1 * len(self.mode):]
                    self.update_mode_required_cached = self.update_mode_required_cached or self.mode != backup_mode

        return self.update_mode_required_cached

    def backup_original_source(self):
        """Create a copy of the original configuration file."""
        try:
            read_fh = open(self.source, "r")
            try:
                write_fh = open(self.backup_source, "w")
                write_fh.writelines(read_fh.readlines())
                write_fh.close()

                if self.mode:
                    chmod(self.backup_source, int("0o%s" % self.mode, 8))
            except Exception as error:
                self.module.fail_json(msg="Failed to create default copy of the original configuration file!"
                                          " Source: [%s]. Destination: [%s]."
                                          " Error [%s]." % (self.source, self.backup_source, error))
        except Exception as error:
            self.module.fail_json(msg="Failed to open source configuration file! Source [%s]."
                                      " Error [%s]." % (self.path, error))

    def update_configuration_file(self):
        """Write copy to the destination."""
        try:
            fh = open(self.destination, "w")
            fh.writelines(self.updated_copy)
            fh.close()

            if self.mode:
                chmod(self.destination, int("0o%s" % self.mode, 8))
        except Exception as error:
            self.module.fail_json(msg="Failed to write configuration file! Destination [%s]."
                                      " Error [%s]." % (self.destination, error))

    def update_mode(self):
        """Change the configuration file's permissions."""
        try:
            chmod(self.destination, int("0o%s" % self.mode, 8))
            chmod(self.backup_source, int("0o%s" % self.mode, 8))
        except Exception as error:
            self.module.fail_json(msg="Failed to change the configuration file permissions! File [%s]."
                                      " Permission [%s]. Error [%s]." % (self.source, self.mode, error))

    def apply(self):
        """Determine and apply any required change to a copy of the source conf file."""
        exit_message = "No changes required."
        changed_required = False

        if not exists(self.source) or not isfile(self.source):
            self.module.fail_json(msg="Invalid configuration path was provided! Source [%s]." % self.source)

        if (self.backup_original_source_required or self.update_configuration_file_required or
             self.update_mode_required):
            changed_required = True

        if changed_required and not self.module.check_mode:
            exit_message = ""
            if self.backup_original_source_required:
                self.backup_original_source()
                exit_message = "Source backup was created. "

            if self.update_configuration_file_required:
                self.update_configuration_file()
                exit_message = exit_message + "Configuration file was changed. "

            if self.update_mode_required:
                self.update_mode()
                exit_message = exit_message + "Configuration file permissions were changed."

        self.module.exit_json(msg=exit_message, source=self.source, backup=self.backup_source,
                              destination=self.destination, changed=changed_required)

def main():
    update_conf = UpdateConfigFile()
    update_conf.apply()


if __name__ == "__main__":
    main()
