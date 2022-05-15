# netapp_eseries.host.ib
    Install and configure packages required for InfiniBand.

## Role Variables
    eseries_ib_interfaces:
        - name:                   # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
          mstconfig:              # Dictionary containing any key-value options for mstconfig to apply to interface.
                                  #   mstconfig is a tool for burning Mellanox HCA cards that is include in mstflint,
                                  #   an open source package that is a subset of the Mellanox Firmware Tools (MFT).
                                  #   For more details checkout the [MFT documentation](https://docs.nvidia.com/networking/display/MFTV4133/MFT+Supported+Configurations+and+Parameters)
            LINK_TYPE_PX: ib      # LINK_TYPE_P1, LINK_TYPE_P2, ..., LINK_TYPE_PX are used to configure the port's
                                  #   working mode. Note that X must match the HCA's port number for the interface which
                                  #   can be determined by 'grep PCI_SLOT_NAME /sys/class/net/<INTERFACE_NAME>/device/uevent',
                                  #   adding 1 to the last number from the PCI slot name and converting to decimal.
                                  #     Example: PCI_SLOT_NAME=0000:2f:00.2 (2 + 1 -> HCA port 3) -> LINK_TYPE_P3: ib

    eseries_ib_skip:              # Whether we should skip configuring InfiniBand entirely (Default: false).
                                  #   Useful to just use functionality provided by other roles that inherit
                                  #   this one when IB is already setup.

    eseries_ib_udev_name:         # Filename for applying eseries_ib_udev_rules
    eseries_ib_udev_rules:        # Dictionary containing interface PCI slots to interface names for ensuring
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
