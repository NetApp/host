# netapp_eseries.host.ib_iser
    This role will install and configure required packages needed to communicate with NetApp E-Series storage using the
    InfiniBand iSER protocol.

## Role Variables
    eseries_ib_iser_configure_network:       # Whether to configure iSCSI network interfaces.
                                             #    Choices: true, false (Default: true)
    eseries_ib_iser_configure_firewall:      # Whether to configure firewall.
                                             #    Choices true, false (Default: true)
    eseries_ib_iser_interfaces:              # (Required) List of IP-based interfaces.
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
        mstconfig:                           # Dictionary containing any key-value options for mstconfig to apply to interface.
                                             #   mstconfig is a tool for burning Mellanox HCA cards that is include in   
                                             #   mstflint, an open source package that is a subset of the Mellanox 
                                             #   Firmware Tools (MFT). For more details checkout the [MFT documentation]
                                             #   (https://docs.nvidia.com/networking/display/MFTV4133/MFT+Supported+Configurations+and+Parameters)
        iface:                               # Dictionary defining additional interface information for
                                             #   open-iscsi (<iscsi_dir>/iface/<interface>).
        node:                                # Dictionary defining additional targets information for open-iscsi
                                             #   (<iscsi_dir>/nodes/<target_iqn>/<address>,<port>,[0-9]+/<interface>).
                                             #   Look at /etc/iscsi/iscsid.conf for options.
    eseries_ib_iser_interface_common:        # Dictionary of common interface definitions for eseries_ib_iser_interfaces.
    eseries_iscsi_iqn:                       # ISCSI qualified name (iqn)
    eseries_ib_iser_default_hook_templates:  # Default list of hook templates for Network Manager dispatcher. Hooks
                                             #   will be applied for individual interfaces.
                                             #   Note: eseries_ip_interfaces entry definition will be accessible
                                             #   through the interface variable within the hook templates.
                                             #   See 99-multihoming.j2 in role's templates directory for an example.
    eseries_ib_iser_firewall_zone:           # Default firewall zone. (Note: Only implemented for firewalld)
    eseries_ib_iser_udev_name:               # Filename for applying eseries_ib_iser_udev_rules
    eseries_ib_iser_udev_rules:              # Dictionary containing interface PCI slots names or MAC addresses to interface names
                                             #    for ensuring persistent interface names.
                                             #   Example: {"0000:2f:00.0": i1a, "0000:2f:00.1": i1b,
                                             #             "0000:86:00.0": i2a, "0000:86:00.1": i2b}
    eseries_ib_iser_uninstall:               # Whether to uninstall the ib_iser role. (Default: false)

## General Notes
    It is recommended to call netapp_eseries.host.storage_setup instead of calling supporting roles directly
    which will configure all related protocols based on storage mapped to the targeted host. However, if you
    need to call this role directly, be sure to set the include_role public option to true. This is important
    to ensure role defaults are available when passed to other supporting roles. All defaults are prefixed with
    eseries_ib_iser_* to prevent variable conflicts with other roles.

    - name: Ensure InfiniBand iSER protocol has been setup
      ansible.builtin.include_role:
        name: netapp_eseries.host.ib_iser
        public: true

## Known Issues
### Enforcing SELinux security causes InfiniBand interfaces to not be available
    This role has a known issue with SELinux that prevents InfiniBand interfaces from functioning properly.

    The symptoms and signature of the issue are:
    - The automation fails due to no usuable iSCSI targets found
    - The communication between the host and array reported unreachable
    - ibstat command would show "State: Initializing" and "Physical state: LinkUp" on all of the InfiniBand interfaces
    - The kernel logs (dmesg -T | grep audit) show the below signature:
        kernel: infiniband mlx5_0: Couldn't open port 1 for agents
        kernel: audit: type=1400 audit(1656357157.949:4): avc: denied { manage_subnet } for pid=7176 comm="systemd-modules" 
        device=mlx5_0 port_num=1 scontext=system_u:system_r:systemd_modules_load_t:s0 tcontext=system_u:object_r:unlabeled_t:s0 
        tclass=infiniband_endport permissive=0
        kernel: infiniband mlx5_2: Couldn't open port 1 for agents
        kernel: audit: type=1400 audit(1656357158.002:5): avc: denied { manage_subnet } for pid=7176 comm="systemd-modules" device=mlx5_2 port_num=1 scontext=system_u:system_r:systemd_modules_load_t:s0 tcontext=system_u:object_r:unlabeled_t:s0 tclass=infiniband_endport permissive=0

    To workaround the issue, either at the prompt during the automation or set the `eseries_selinux_state` variable in 
    your inventory to 'disabled' or 'permissive'.

    Additionally, if the automation was executed with "enforcing" initially and then re-ran with "permissive", the link 
    may not come up still. This is due to opensm service is already running and doesn't get updated when the 
    selinux policy is changed. The automation is cautious when having to restart your service/host, therefore, the
    below recovery steps to bring up the InfiniBand links need to be done manually.
    Follow one of the workaround options below:
    1) Unload and reload the "mlx5_ib" driver and restart the opensm service
        $ modprobe -r mlx5_ib
        $ modprobe mlx5_ib
        $ systemctl restart opensm
    2) Reboot the host

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
