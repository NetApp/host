# netapp_eseries.host.iscsi
    This role will install and configure required packages needed to communicate with NetApp E-Series storage using the
    iSCSI protocol.

## Role Variables
    eseries_iscsi_configure_network:         # Whether to configure iSCSI network interfaces.
                                             #    Choices: true, false (Default: true)
    eseries_iscsi_configure_firewall:        # Whether to configure firewall.
                                             #    Choices true, false (Default: true)
    eseries_iscsi_interfaces:                # (Required) List of IP-based interfaces.
      - name:                                # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                             # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                      # List of hook templates for Network Manager dispatcher.
                                             #   Note: eseries_ip_interfaces entry definition will be accessible through
                                             #   the interface variable within the hook templates.
                                             #   See 99-multihoming.j2 in role's templates directory for an example.
        zone:                                # Firewall zone. If the zone does not exist then it will be created.
                                             #   Note: Only implemented for firewalld
        (...)                                # Add any valid key-value pair for the expected Netplan or ifupdown
                                             #   configuration files. Be sure to quote recognized boolean values (on,
                                             #   off, yes, no, etc.) otherwise they will be converted into True/False.
        iface:                               # Dictionary defining additional interface information for
                                             #   open-iscsi (<iscsi_dir>/iface/<interface>).
        node:                                # Dictionary defining additional targets information for open-iscsi
                                             #   (<iscsi_dir>/nodes/<target_iqn>/<address>,<port>,[0-9]+/<interface>).
                                             #   Look at /etc/iscsi/iscsid.conf for options.
    eseries_iscsi_interface_common:          # Dictionary of common interface definitions for eseries_iscsi_interfaces.
    eseries_iscsi_iqn:                       # ISCSI qualified name (iqn)
    eseries_iscsi_default_hook_templates:    # Default list of hook templates for Network Manager dispatcher. Hooks will be
                                             #   applied for individual interfaces.
                                             #   Note: eseries_ip_interfaces entry definition will be accessible
                                             #   through the interface variable within the hook templates.
                                             #   See 99-multihoming.j2 in role's templates directory for an example.
    eseries_iscsi_firewall_zone:             # Default firewall zone. (Note: Only implemented for firewalld)
    eseries_iscsi_udev_name:                 # Filename for applying eseries_iscsi_udev_rules
    eseries_iscsi_udev_rules:                # Dictionary containing interface PCI slots to interface names for ensuring
                                             #   persistent interface names.
                                             #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                             #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}

## Notes
    WARNING! Role will configure the specified iSCSI network interfaces unless eseries_iscsi_configure_network is set to false.
    Note: Reduction in session will only be configured but not applied.

## Uninstall
    To uninstall, add '--tags iscsi_uninstall' to the ansible-playbook command or import uninstall.yml task directly
    from role.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
