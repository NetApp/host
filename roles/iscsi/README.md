# netapp_eseries.host.iscsi

## Role Variables
    eseries_iscsi_configure_network:         # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
    eseries_iscsi_configure_firewall:        # Whether to configure firewall. Choices true, false (Default: true)
    eseries_iscsi_interfaces:                # (Required) List of IP-based interfaces.
      - name:                                # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                             # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                      # List of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                             #   the interface variable within the hook templates).
        zone:                                # Firewall zone. If the zone does not exist then it will be created. (Note: Only implemented for firewalld)
        (...)                                # Add any valid key-value pair for the expected Netplan or ifcfg-x configuration files. Be sure to quote recognized
                                             #   boolean values (on, off, yes, no, etc.) otherwise they will be converted into True/False.
        iface:                               # Dictionary defining additional interface information for open-iscsi (<iscsi_dir>/iface/<interface>).
        node:                                # Dictionary defining additional targets information for open-iscsi (<iscsi_dir>/nodes/<target_iqn>/<address>,<port>,[0-9]+/<interface>).
                                             #   Look at /etc/iscsi/iscsid.conf for options.
    eseries_iscsi_default_hook_templates:    # Default list of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                             #    the interface variable within the hook templates).
    eseries_iscsi_firewall_zone:             # Default firewall zone. (Note: Only implemented for firewalld)

## Notes
    WARNING! Role will configure the specified iSCSI network interfaces unless eseries_iscsi_configure_network is set to false.
    Note: Reduction in session will only be configured but not applied.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
