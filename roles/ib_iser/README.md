# netapp_eseries.host.ib_iser
    Ensure InfiniBand iSER is configured on host.

## Role Variables
    eseries_iscsi_iqn:                          # Host IQN (iSCSI Qualified Name).
    eseries_ib_iser_configure_network:          # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
    eseries_ib_iser_configure_firewall:         # Whether to configure firewall. Choices true, false (Default: true)
    eseries_ib_iser_interfaces:                 # (Required) List of IP-based interfaces.
      - name:                                   # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                                # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                         # List of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                                #   the interface variable within the hook templates).
        zone:                                   # Firewall zone. If the zone does not exist then it will be created. (Note: Only implemented for firewalld)
        (...)                                   # Add any valid key-value pair for the expected Netplan or ifcfg-x configuration files. Be sure to quote recognized
                                                #   boolean values (on, off, yes, no, etc.) otherwise they will be converted into True/False.
        iface:                                  # Dictionary defining additional interface binding information for open-iscsi (<iscsi_dir>/iface/<interface>).
        node:                                   # Dictionary defining additional target information for open-iscsi (<iscsi_dir>/nodes/<target_iqn>/<address>,<port>,[0-9]+/<interface>).
                                                #   Look at /etc/iscsi/iscsid.conf for options.
    eseries_ib_iser_default_hook_templates:     # Default list of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                                #    the interface variable within the hook templates).
    eseries_ib_iser_firewall_zone:              # Default firewall zone. (Note: Only implemented for firewalld)
    eseries_ib_iser_iscsid_conf_options:        # Dictionary containing option-value pairs for open-iscsi global configuration options for Ansible node (iscsid.conf).
    eseries_ib_iser_iscsid_conf_group_options:  # Dictionary containing option-value pairs for open-iscsi global configuration options for Ansible group (iscsid.conf).
    eseries_ib_iser_iface_options:              # Dictionary containing option-value pairs for open-iscsi interface bindings for Ansible node.
    eseries_ib_iser_iface_group_options:        # Dictionary containing option-value pairs for open-iscsi interface bindings for Ansible group.
    eseries_ib_iser_node_options:               # Dictionary containing option-value pairs for open-iscsi target node information for Ansible node.
    eseries_ib_iser_node_group_options:         # Dictionary containing option-value pairs for open-iscsi target node information for Ansible group.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)