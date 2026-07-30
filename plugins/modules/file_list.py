#!/usr/bin/python

# (c) NetApp, Inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: file_list
short_description: Update log file containing comma separated list.
description:
    - Add and remove items to comma separated list found in log file.
author: Nathan Swartz (@ndswartz)
options:
    file:
        description: Absolute file path on remote system
        required: True
        type: str
    items:
        description: Item(s) to add or remove from file.
        required: False
        type: list
        elements: str
    mode:
        description: Whether to add or remove items.
        required: True
        choices: ["add", "remove", "content"]
        type: str
"""

EXAMPLES = """
- update_file_list:
    mode: add
    file: /var/log/test
    items:
      - item3
      - item4
- update_file_list:
    mode: remove
    file: /var/log/test
    items:
      - item2
      - item3
      - item5
"""

RETURN = """
msg:
    description: Success message
    returned: always
    type: str
changed:
    description: Whether change was made to the log file.
    returned: always
    type: str
list:
    description: List of items in comma separated list
    returned: always
    type: list
"""
from ansible.module_utils.basic import AnsibleModule


class UpdateFileList(object):
    def __init__(self):
        ansible_options = dict(mode=dict(type='str', required=True, choices=["add", "remove", "content"]),
                               file=dict(type='str', required=True),
                               items=dict(type='list', required=False, elements='str'))

        required_if = [["mode", "add", ["items"]], ["mode", "remove", ["items"]]]
        self.module = AnsibleModule(argument_spec=ansible_options, required_if=required_if, supports_check_mode=True)

        args = self.module.params
        self.mode = args["mode"]
        self.file = args["file"]
        self.items_list = set()
        self.items = set()
        if self.mode in ["add", "remove"]:
            for item in args["items"]:
                self.items.add(item)

    def add(self):
        """Add item(s) to list."""
        for item in self.items:
            if item not in self.items_list:
                self.items_list.add(item)

    def remove(self):
        """Remove item(s) from list."""
        for item in self.items:
            if item in self.items_list:
                self.items_list.remove(item)

    def update(self):
        """Initiate the file update."""
        try:
            fh = open(self.file, "r")
            item_list = fh.read()
            for item in item_list.split("\n"):
                if item:
                    self.items_list.add(item)
        except IOError as error:
            pass

        update_required = False
        if self.items:
            if self.mode == "add":
                for item in self.items:
                    if item not in self.items_list:
                        update_required = True
            elif self.mode == "remove":
                for item in self.items:
                    if item in self.items_list:
                        update_required = True

        if update_required and not self.module.check_mode:
            if self.mode == "add":
                self.add()
            elif self.mode == "remove":
                self.remove()

            with open(self.file, "w") as fh:
                fh.write("\n".join(self.items_list))

        self.module.exit_json(msg="List is up to date.", list=self.items_list, changed=update_required)


def main():
    item_list = UpdateFileList()
    item_list.update()


if __name__ == '__main__':
    main()
