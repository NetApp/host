# netapp_eseries.host.ib
    Install and configure packages required for InfiniBand.

## Role Variables

    eseries_ib_skip:                # Whether we should skip configuring InfiniBand entirely (Default: false).
                                    #   Useful to just use functionality provided by other roles that inherit
                                    #   this one when IB is already setup.

    eseries_ib_udev_name:               # Filename for applying eseries_ib_udev_rules
    eseries_ib_udev_rules:              # Dictionary containing interface PCI slots to interface names for ensuring
                                        #   persistent interface names.
                                        #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                        #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}

## Uninstall
    To uninstall, add '--tags ib_base_uninstall' to the ansible-playbook command or import uninstall.yml task directly
    from role. `ansible-playbook -i inventory.yml playbook --tags ib_base_uninstall`

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
