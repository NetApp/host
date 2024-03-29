# netapp_eseries.host.selinux
    Configure SELinux on host.

## Role Variables
    eseries_selinux_config:          # Path to SELinux configuration file. Default: /etc/selinux/config
    eseries_selinux_state:           # Whether SELinux security should be enabled. Choices:
                                     #   enforcing - SELinux security policy is enforced.
                                     #   permissive - SELinux prints warnings instead of enforcing.
                                     #   disabled - No SELinux policy is loaded.
    eseries_selinux_policy:          # SELinux security policy. The policy will not be changed unless
                                     #   `eseries_selinux_policy` is defined. There may be other policies
                                     #    but the following are common choices.
                                     #      targeted - Targeted processes are protected,
                                     #      minimum - Modification of targeted policy. Only selected processes are protected.
                                     #      mls - Multi Level Security protection.
    eseries_selinux_prompt_reason:   # The reason to prompt user's for eseries_selinux_state when not defined such as
                                     #   when SELinux results in issues that need to be resolved manually.

## General Note
    - This role will not install SELinux packages and will only configure SELinux when installed.
    - This role requires `eseries_selinux_state` to be defined and will provide a prompt should one not be provided.

## License
    BSD-3-Clause

# Author Information
    Nathan Swartz (@ndswartz)
