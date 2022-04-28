# netapp_eseries.host.ip_base

## Role Variables
    eseries_ip_base_interfaces:              # (Required) List of IP-based interfaces. Be sure to quote values that will be converted into a boolean
                                             #   value (on, off, yes, no, etc.) otherwise they will be converted into True/False.
      - name:                                # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                             # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                      # List of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                             #   the item["interface"] dictionary within the hook templates).
        zone:                                # Firewall zone. If the zone does not exist then it will be created. (Note: Only implemented for firewalld)
        (...)                                # Add any valid key-value pair for the expected Netplan or ifupdown configuration files.
    eseries_ip_base_interface_common:        # Dictionary containing any common valid key-value pair for Netplan or ifupdown configuration files. Be
                                             #   sure to quote values that will be converted into a boolean value (on, off, yes, no, etc.) otherwise
                                             #   they will be converted into True/False.
    eseries_ip_base_configure_network:       # Whether to configure network interfaces. Choices: true, false (Default: true)
    eseries_ip_base_configure_firewall:      # Whether to configure firewall for network interfaces. Choices: true, false (Default: true)
    eseries_ip_base_manager_tools:           # List of network manager tools that are being used. Only required if Netplan and an ifupdown compatible
                                             #   tool are both installed or NetworkManager and systemd-networkd are both installed.
                                             #   Choices: [netplan/ifupdown, network_manager/networkd]
    eseries_ip_base_interface_type:          # Interface type as defined for ifupdown files. Default: Ethernet
    eseries_ip_base_default_hook_templates:  # Default list of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                             #    the interface variable within the hook templates).

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
