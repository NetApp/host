# netapp_eseries.host.ip
    Configure network interface IP addresses, names, and implement hooks.

## Role Variables
    eseries_ip_interfaces:              # (Required) List of IP-based interfaces. Be sure to quote values that will be
                                        #   converted into a boolean value (on, off, yes, no, etc.) otherwise they will
                                        #   be converted into True/False.
      - name:                           # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                        # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                 # List of hook templates for Network Manager dispatcher.
                                        #   Note: eseries_ip_interfaces entry definition will be accessible through
                                        #   the interface variable within the hook templates.
                                        #   See 99-multihoming.j2 in role's templates directory for an example.
        zone:                           # Firewall zone. If the zone does not exist then it will be created.
                                        #   Note: Only implemented for firewalld
        (...)                           # Add any valid key-value pair for the expected Netplan or ifupdown
                                        #   configuration files.
    eseries_ip_interface_common:        # Dictionary containing any common valid key-value pair for Netplan or ifupdown
                                        #   configuration files. Be sure to quote values that will be converted into a
                                        #   boolean value (on, off, yes, no, etc.) otherwise they will be converted
                                        #   into True/False.
    eseries_ip_configure_network:       # Whether to configure network interfaces. Choices: true, false (Default: true)
    eseries_ip_configure_firewall:      # Whether to configure firewall for network interfaces.
                                        #   Choices: true, false (Default: true)
    eseries_ip_manager_tools:           # List of network manager tools that are being used. Only required if Netplan
                                        #   and an ifupdown or nmcli compatible tool are both installed or NetworkManager and
                                        #   systemd-networkd are both installed.
                                        #   Choices: [netplan/ifupdown/nmcli, network_manager/networkd]
    eseries_ip_interface_type:          # Interface type as defined for ifupdown files.
                                        #   Choices: Ethernet, InfiniBand (Default: Ethernet)
    eseries_ip_default_hook_templates:  # Default list of hook templates for Network Manager dispatcher. Hooks will be
                                        #   applied for individual interfaces.
                                        #   Note: eseries_ip_interfaces entry definition will be accessible through
                                        #   the interface variable within the hook templates.
                                        #   See 99-multihoming.j2 in role's templates directory for an example.

    eseries_ip_udev_name:               # Filename for applying eseries_ip_udev_rules
    eseries_ip_udev_rules:              # Dictionary containing interface PCI slots names or MAC addresses to interface names
                                        #   for ensuring persistent interface names.
                                        #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                        #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
