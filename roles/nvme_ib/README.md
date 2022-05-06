# netapp_eseries.host.nvme_ib
    This role will install and configure required packages needed to communicate with NetApp E-Series storage using the
    NVMe over InfiniBand protocol.

## Role Variables
    eseries_nvme_nqn:                        # Host NQN. When not specified, nqn will be derived from host.
    eseries_nvme_ib_interfaces:              # (Required) List of IP-based interfaces. Be sure to quote values that will
                                             #   be converted into a boolean value (on, off, yes, no, etc.) otherwise
                                             #   they will be converted into True/False.
      - name:                                # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                             # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                      # List of hook templates for Network Manager dispatcher.
                                             #   Note: eseries_ip_interfaces entry definition will be accessible through
                                             #   the interface variable within the hook templates.
                                             #   See 99-multihoming.j2 in role's templates directory for an example.
        zone:                                # Firewall zone. If the zone does not exist then it will be created.
                                             #    Note: Only implemented for firewalld
        (...)                                # Add any valid key-value pair for the expected Netplan or ifcfg-x
                                             #    configuration files.
        configure:                           # Whether to configure OpenSM for interface.
        subnet_prefix:                       # OpenSM subnet manager's subnet prefix.
        priority:                            # OpenSM subnet manager's priority.
    eseries_nvme_ib_interface_common:        # Dictionary containing any common valid key-value pair for Netplan or
                                             #   ifcfg-x configuration files. Be sure to quote values that will be
                                             #   converted into a boolean value (on, off, yes, no, etc.) otherwise
                                             #   they will be converted into True/False.
    eseries_nvme_ib_configure_network:       # Whether to configure network interfaces.
                                             #    Choices: true, false (Default: true)
    eseries_nvme_ib_configure_firewall:      # Whether to configure firewall for network interfaces.
                                             #    Choices: true, false (Default: true)
    eseries_nvme_ib_default_hook_templates:  # Default list of hook templates for Network Manager dispatcher. Hooks will
                                             #   be applied for individual interfaces.
                                             #   Note: eseries_ip_interfaces entry definition will be accessible through
                                             #   the interface variable within the hook templates.
                                             #   See 99-multihoming.j2 in role's templates directory for an example.
    eseries_nvme_ib_udev_name:               # Filename for applying eseries_nvme_ib_udev_rules
    eseries_nvme_ib_udev_rules:              # Dictionary containing interface PCI slots to interface names for ensuring
                                             #   persistent interface names.
                                             #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                             #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}

## General Notes
    A customized systemd service daemon will be generated based on the required targets needed for existing storage system mappings. You can view the generated daemon at /etc/nvme/eseries_nvme_ib_daemon. The daemon is controlled with the systemd service eseries_nvme_ib.service which will ensure connectivity during boot.

## Uninstall
    To uninstall NVMe over InfiniBand, add '--tags nvme_ib_uninstall' to the ansible-playbook command or import uninstall.yml task directly
    from role.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
