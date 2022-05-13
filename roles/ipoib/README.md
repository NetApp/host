# netapp_eseries.host.ipoib
    This role will setup IP over InfiniBand which installs and configure required InfiniBand packages, kernel modules,
    and configures network interfaces using either ifcfg-x configuration files or netplan.

## Role Variables
    eseries_ipoib_interfaces:              # (Required) List of IP-based interfaces. Be sure to quote values that will
                                           #   be converted into a boolean value (on, off, yes, no, etc.) otherwise
                                           #   they will be converted into True/False.
      - name:                              # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                           # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                    # List of hook templates for Network Manager dispatcher.
                                           #   Note: eseries_ip_interfaces entry definition will be accessible through
                                           #   the interface variable within the hook templates.
                                           #   See 99-multihoming.j2 in role's templates directory for an example.
        zone:                              # Firewall zone. If the zone does not exist then it will be created.
                                           #    Note: Only implemented for firewalld
        (...)                              # Add any valid key-value pair for the expected Netplan or ifcfg-x
                                           #    configuration files.
        mstconfig:                         # Dictionary containing any key-value options for mstconfig to apply to interface.
                                           #   mstconfig is a tool for burning Mellanox HCA cards that is include in mstflint,
                                           #   an open source package that is a subset of the Mellanox Firmware Tools (MFT).
                                           #   For more details checkout the [MFT documentation](https://docs.nvidia.com/networking/display/MFTV4133/MFT+Supported+Configurations+and+Parameters)
    eseries_ipoib_interface_common:        # Dictionary containing any common valid key-value pair for Netplan or
                                           #   ifcfg-x configuration files. Be sure to quote values that will be
                                           #   converted into a boolean value (on, off, yes, no, etc.) otherwise
                                           #   they will be converted into True/False.
    eseries_ipoib_configure_network:       # Whether to configure network interfaces.
                                           #    Choices: true, false (Default: true)
    eseries_ipoib_configure_firewall:      # Whether to configure firewall for network interfaces.
                                           #    Choices: true, false (Default: true)
    eseries_ipoib_default_hook_templates:  # Default list of hook templates for Network Manager dispatcher. Hooks will
                                           #   be applied for individual interfaces.
                                           #   Note: eseries_ip_interfaces entry definition will be accessible through
                                           #   the interface variable within the hook templates.
                                           #   See 99-multihoming.j2 in role's templates directory for an example.
    eseries_ipoib_udev_name:               # Filename for applying eseries_ipoib_udev_rules
    eseries_ipoib_udev_rules:              # Dictionary containing interface PCI slots to interface names for ensuring
                                           #   persistent interface names.
                                           #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                           #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}

## Uninstall
    To uninstall InfiniBand IPoIB, add '--tags ipoib_uninstall' to the ansible-playbook command or import uninstall.yml task directly
    from role.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
