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
        mstconfig:                           # Dictionary containing any key-value options for mstconfig to apply to interface.
                                             #   mstconfig is a tool for burning Mellanox HCA cards that is include in mstflint,
                                             #   an open source package that is a subset of the Mellanox Firmware Tools (MFT).
                                             #   For more details checkout the [MFT documentation](https://docs.nvidia.com/networking/display/MFTV4133/MFT+Supported+Configurations+and+Parameters)
            LINK_TYPE_PX: ib                 # LINK_TYPE_P1, LINK_TYPE_P2, ..., LINK_TYPE_PX are used to configure the port's
                                             #   working mode. Note that X must match the HCA's port number for the interface which
                                             #   can be determined by 'grep PCI_SLOT_NAME /sys/class/net/<INTERFACE_NAME>/device/uevent',
                                             #   adding 1 to the last number from the PCI slot name and converting to decimal.
                                             #     Example: PCI_SLOT_NAME=0000:2f:00.2 (2 + 1 -> HCA port 3) -> LINK_TYPE_P3: ib
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
    eseries_nvme_ib_udev_rules:              # Dictionary containing interface PCI slots names or MAC addresses to interface names
                                             #   for ensuring persistent interface names.
                                             #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                             #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}
    eseries_nvme_ib_uninstall:               # Whether to uninstall the nvme_ib role. (Default: false)


## General Notes
    It is recommended to call netapp_eseries.host.storage_setup instead of calling supporting roles directly
    which will configure all related protocols based on storage mapped to the targeted host. However, if you
    need to call this role directly, be sure to set the include_role public option to true. This is important
    to ensure role defaults are available when passed to other supporting roles. All defaults are prefixed with
    eseries_nvme_ib_* to prevent variable conflicts with other roles.

    - name: Ensure NVMe over InfiniBand protocol has been setup
      ansible.builtin.include_role:
        name: netapp_eseries.host.nvme_ib
        public: true

    A customized systemd service daemon will be generated based on the required targets needed for existing storage system mappings. You can view the generated daemon at /etc/nvme/eseries_nvme_ib_daemon. The daemon is controlled with the systemd service eseries_nvme_ib.service which will ensure connectivity during boot.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
