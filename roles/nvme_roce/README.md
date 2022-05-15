# netapp_eseries.host.nvme_roce
    Ensure NVMe RoCE is configured on host.

## Role Variables
    eseries_nvme_roce_configure_network:         # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
    eseries_nvme_roce_configure_firewall:        # Whether to configure firewall. Choices true, false (Default: true)
    eseries_nvme_roce_interfaces:                # (Required) List of IP-based interfaces.
      - name:                                    # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                                 # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                          # List of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                                 #   the interface variable within the hook templates).
        zone:                                    # Firewall zone. If the zone does not exist then it will be created. (Note: Only implemented for firewalld)
        (...)                                    # Add any valid key-value pair for the expected Netplan or ifcfg-x configuration files. Be sure to quote recognized
                                                 #   boolean values (on, off, yes, no, etc.) otherwise they will be converted into True/False.
        mstconfig:                               # Dictionary containing any key-value options for mstconfig to apply to interface.
                                                 #   mstconfig is a tool for burning Mellanox HCA cards that is include in mstflint,
                                                 #   an open source package that is a subset of the Mellanox Firmware Tools (MFT).
                                                 #   For more details checkout the [MFT documentation](https://docs.nvidia.com/networking/display/MFTV4133/MFT+Supported+Configurations+and+Parameters)
          LINK_TYPE_PX: eth                      # LINK_TYPE_P1, LINK_TYPE_P2, ..., LINK_TYPE_PX are used to configure the port's
                                                 #   working mode. Note that X must match the HCA's port number for the interface which
                                                 #   can be determined by 'grep PCI_SLOT_NAME /sys/class/net/<INTERFACE_NAME>/device/uevent',
                                                 #   adding 1 to the last number from the PCI slot name and converting to decimal.
                                                 #     Example: PCI_SLOT_NAME=0000:2f:00.2 (2 + 1 -> HCA port 3) -> LINK_TYPE_P3: eth
    eseries_nvme_roce_interface_common:          # Dictionary containing any common valid key-value pair for Netplan or ifupdown configuration files. Be sure to quote
                                                 #   values that will be converted into a boolean value (on, off, yes, no, etc.) otherwise they will be converted
                                                 #   into True/False.
    eseries_nvme_roce_default_hook_templates:    # Default list of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                                 #    the interface variable within the hook templates).
    eseries_nvme_roce_firewall_zone:             # Default firewall zone. (Note: Only implemented for firewalld)
    eseries_nvme_roce_nqn:                       # Host NVMe qualified name.
    eseries_nvme_roce_udev_name:                 # Filename for applying eseries_nvme_roce_udev_rules
    eseries_nvme_roce_udev_rules:                # Dictionary containing interface PCI slots to interface names for ensuring persistent interface names.
                                                 #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                                 #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}

## Uninstall
    To uninstall, add '--tags nvme_roce_uninstall' to the ansible-playbook command or import uninstall.yml task directly
    from role.

## Notes
    WARNING! Role will configure the specified network interfaces unless eseries_nvme_roce_configure_network is set to false.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
