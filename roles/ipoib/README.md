# netapp_eseries.host.ipoib
    Configures IP over InfiniBand which installs and configure packages, kernel modules, and configures network interfaces using either ifupdown or netplan.

## Role Variables
    eseries_ipoib_interfaces:              # (Required) List of IP-based interfaces. Be sure to quote values that will be converted into a boolean
                                           #   value (on, off, yes, no, etc.) otherwise they will be converted into True/False.
      - name:                              # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                           # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                    # List of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                           #   the item["interface"] dictionary within the hook templates).
        zone:                              # Firewall zone. If the zone does not exist then it will be created. (Note: Only implemented for firewalld)
        (...)                              # Add any valid key-value pair for the expected Netplan or ifcfg-x configuration files.
    eseries_ipoib_interface_common:        # Dictionary containing any common valid key-value pair for Netplan or ifcfg-x configuration files. Be
                                           #   sure to quote values that will be converted into a boolean value (on, off, yes, no, etc.) otherwise
                                           #   they will be converted into True/False.
    eseries_ipoib_configure_network:       # Whether to configure network interfaces. Choices: true, false (Default: true)
    eseries_ipoib_configure_firewall:      # Whether to configure firewall for network interfaces. Choices: true, false (Default: true)
    eseries_ipoib_interface_type:          # Interface type as defined for ifcfg-x files. Default: InfiniBand
    eseries_ipoib_default_hook_templates:  # Default list of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                           #    the interface variable within the hook templates).

## Uninstall
    To uninstall InfiniBand IPoIB, add '--tags ipoib_uninstall' to the ansible-playbook command.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
