NetApp E-Series Host Collection
===============================
    NetApp E-Series Host collection consist of the latest available host utility roles relating to E-Series platforms.

    The roles in this collection can be used to configure your host storage connection for iSCSI, InfiniBand, and NVMe; Discover mapped E-Series volumes, format them to your specifications, and assign persistent mount points to them.

    Roles:
        - mount: Format and assign persistent mount points to your mapped E-Series volumes.
        - multipath: Install and configure multipath.
        - protocol: Automatically installs the required protocols on the host. This will call the required protocol roles (iscsi, ib_iser, etc).
        - sanitize_volume: Delete, unmapped, and wipe format metadata from volumes on host.
        - common: Collect storage system information, discover volumes on storage system, and spin up local docker web services proxy instance.
        - iscsi: Configures the iSCSI protocol which configures network interfaces (ifupdown or netplan), installs and configures required packages, and establishes sessions.
        - ipoib: Configures IP over InfiniBand which installs and configure packages, kernel modules, configures network interfaces (ifupdown or netplan), and configures InfiniBand subnet manager if needed.
        - ib_iser: Configures the InfiniBand iSER protocol which configures network interfaces (ifupdown or netplan), installs and configures required packages, and establishes sessions.
        - fc: Not implemented.
        - ib_srp: Not implemented yet.
        - nvme_fc: Not implemented yet.
        - nvme_ib: Not implemented yet.
        - nvme_roce: Not implemented yet.
        - sas: Not implemented yet.

    Tested Platforms:
        - RHEL 7.7
        - SLES 12sp4
        - Ubuntu 16.04 LTS (iSCSI only)
        - Ubuntu 18.04 LTS

Requirements
------------
    - Ansible 2.9 or later
    - NetApp E-Series E2800 platform or newer or NetApp E-Series SANtricity Web Services Proxy configured for older E-Series Storage arrays.
    - Python packages: netaddr, ipaddr

iSCSI Host Example Inventory (See iSCSI variables for more options)
----------------------------
    ansible_host: 192.168.1.100
    ansible_ssh_user: ssh_username
    ansible_become_password: ssh_password
    eseries_common_group: eseries_storage_systems
    eseries_iscsi_iqn: iqn.1994-05.com.example:12345
    eseries_iscsi_interfaces:
      - name: eth1
        address: 192.168.1.102/24
      - name: eth2
        address: 192.168.1.104/24

InfiniBand iSER Host Example Inventory (See InfiniBand iSER Role Variables for more options)
--------------------------------------
    ansible_host: 192.168.1.100
    ansible_ssh_user: ssh_username
    ansible_become_password: ssh_password
    eseries_common_group: eseries_storage_systems
    eseries_iscsi_iqn: iqn.1994-05.com.example:12345
    eseries_ib_iser_interfaces:
      - name: ib0
        address: 192.168.2.100/24
      - name: ib1
        address: 192.168.2.101/24

Example Storage System Inventory (Minimum requirements. See netapp_eseries.santricity collection's README.md for more information).
--------------------------------
    eseries_system_api_url: https://192.168.1.200:8443/devmgr/v2/
    eseries_system_password: admin_password
    eseries_validate_certs: false

Example Project
---------------
    See https://github.com/netappeseries/host/tree/master/example_project.

Example Playbook (Ensure mapped-volumes are mounted)
----------------------------------------------------
    - hosts: eseries_host_group
      collections:
        - netapp_eseries.host
      tasks:
        - name: Ensure multipath and protocol requirements are setup and configured.
          import_role:
            name: storage_setup
        - name: Ensure the expected volumes mapped from an E-Series storage system are mounted.
          import_role:
            name: mount

Important Notes
---------------
    When taking advantage of the volume_metadata in the SANtricity collection's nar_santricity_host role, be sure that the host inventory does not conflict with volume_metadata entries. The volume's volume_metadata will take precedence over the host inventory!

*Note: Some variables may be repeated in multiple roles which is done to maintain continuity between roles should the defaults be overwritten.
Common Variables (common)
-------------------------
    eseries_common_group:                            # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
    eseries_common_volume_workload_filter:           # Filters the volumes added to eseries_volumes.
    eseries_common_allow_host_reboot:                # Whether reboots will allowed in an attempt to discover E-Series volumes. (Default: false)
    eseries_common_docker_host:                      # Docker host for SANtricity Web Services Proxy. (Default: unix://var/run/docker.sock)

Multipath Variables (multipath)
-------------------------------
    eseries_multipath_configure_user_friendly_names:   # Ensures that all volumes are presented with their given name. (Default: true)
    eseries_multipath_conf_d_path:                     # The directory path for E-Series specific wwid-alias definitions (Default: /etc/multipath/conf.d/).
    eseries_multipath_kernel_modules:                  # Kernel modules that need to be loaded in order for multipath to be functioning correctly. (Default [dm_multipath])
    eseries_multipath_remove_installation:             # This flag will for multipath to be removed. (Default: false)

Storage_Setup Variables
-----------------------
    eseries_multipath_configure_user_friendly_names:   # Ensures that all volumes are presented with their given name. (Default: true)
    eseries_multipath_conf_d_path:                     # The directory path for E-Series specific wwid-alias definitions. (Default: /etc/multipath/conf.d/)
    eseries_multipath_kernel_modules:                  # Kernel modules that need to be loaded in order for multipath to be functioning correctly. (Default [dm_multipath])
    eseries_multipath_remove_installation:             # This flag will for multipath to be removed. (Default: false)
    eseries_protocol:                                  # Protocols to install which are determined by the storage systems that have mapped volumes. `auto` will
                                                       #   determine which protocols are required.
                                                       #   Choices: auto, fc, ib_iser, ib_srp, iscsi, nvme_fc, nvme_ib, nvme_roce, sas (Default: auto)
    eseries_protocol_log_path:                         # Path to eseries_protocol_log which is used to maintain a record of communication protocols installed. (Default: /var/log/)
    eseries_storage_setup_uninstall:                   # Whether to uninstall multipath and communication protocols. (Default: false)

Mount Variables (mount)
--------------------
    * Note: `VOLUME_SEGMENT_SIZE_KB` and `VOLUME_STRIPE_COUNT` will be replaced with the correct values from your E-Series storage system.
    eseries_mount_volumes:                     # List of volume names to mount. `all_volumes` ensures all mapped volumes are mounted. (Default:["all_volumes"])
    eseries_mount_format_type:                 # Volume format type. (Default: xfs)
    eseries_mount_format_options:              # Volume format options. (Default: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk")
    eseries_mount_persistent_mount_options:    # Volume mount options. (Default: "_netdev")
    eseries_mount_root_directory:              # Volume mount directory. (Default: /mnt/)
    eseries_mount_skip_unmount:                # Whether to skip mounting volumes. (Default: false)
    eseries_mount_format_type_options:         # Mount options for different formats. Used when eseries_mount_format_options is not defined.
                                               # Defaults: xfs: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk"
                                               #           ext4: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk"
                                               #           btrfs: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk"

    *Tip: Add mount_to_hosts, format_type, format_options, mount_dir, mount_options to the volume's volume_metadata tags to provide information for mounting. This can be done with netapp_eseries.santricity.nar_santricity_host role. See SANtricity collection for more details.

Unmount Variables (unmount)
---------------------------
    eseries_common_group:                      # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
    eseries_unmount_volumes:                   # (Required) E-Series volume name list to unmount (Default: []).
    eseries_unmount_purge:                     # Purge volume completely from host (Default: false).
    eseries_unmount_unmap:                     # Unmap E-Series volume from host (Default: false).
    eseries_unmount_delete:                    # Delete E-Series volume from host (Default: false).
    eseries_unmount_wipe_format_signatures:    # Clear the format signatures from the E-Series volume (Default: false)

IP over InfiniBand Variables (ipoib)
------------------------------------
    eseries_ipoib_interfaces:                  # (Required) List of InfiniBand interfaces (Note: Not required if eseries_ib_iser_interfaces is defined).
      - name:                                  # (Required) Name of InfiniBand interface (i.e. ib0, ib1).
        address:                               # (Required) IPv4 address. Use the format 192.0.2.24.
        opensm_configure:                      # Whether to configure OpenSM for port.
        opensm_subnet_prefix:                  # OpenSM subnet manager's subnet prefix.
        opensm_priority:                       # OpenSM subnet manager's priority.
        mtu:                                   # Interface maximum transmission unit measured in bytes.
    eseries_ipoib_mtu:                         # Default maximum transmission unit measured in bytes (Default: "").
    eseries_ipoib_opensm_configure:            # Default for whether to configure OpenSM. eseries_ib_iser_opensm_configure can be used instead (Default: true).
    eseries_ipoib_opensm_subnet_prefix:        # Default OpenSM subnet manager's subnet prefix. eseries_ib_iser_opensm_subnet_prefix can be used instead (Default: "0xfe80000000000000").
    eseries_ipoib_opensm_subnet_priority:      # Default OpenSM subnet manager's priority. eseries_ib_iser_opensm_subnet_priority can be used instead (Default: 0).
    eseries_ipoib_ubuntu_packages:             # Default packages for ubuntu (Default: [rdma-core, infiniband-diags]).
    eseries_ipoib_suse_packages:               # Default packages for ubuntu (Default: [rdma-core, infiniband-diags]).
    eseries_ipoib_rhel_packages:               # Default packages for ubuntu (Default: [rdma-core, infiniband-diags]).
    eseries_ipoib_kernel_modules:              # Default loaded kernel modules (Default: [rdma_cm, mlx5_core, ib_ipoib]).
    eseries_ipoib_uninstall_kernel_modules:    # Default unloaded kernel modules when uninstalled. (Default: [mlx5_ib, mlx5_core, ib_ipoib])

Protocol Variables (protocol)
-----------------------------
    eseries_protocol:             # Protocols to install which are determined by the storage systems that have mapped volumes. `auto` will
                                  #   determine which protocols are required.
                                  #   Choices: auto, fc, ib_iser, ib_srp, iscsi, nvme_fc, nvme_ib, nvme_roce, sas (Default: auto)
    eseries_protocol_log_path:    # Path to eseries_protocol_log which is used to maintain a record of communication protocols installed. (Default: /var/log/)

InfiniBand iSER Variables (ib_iser)
-----------------------------------
    eseries_common_group:                           # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
    eseries_iscsi_iqn:                              # Host IQN (iSCSI Qualified Name).
    eseries_ib_iser_interfaces:                     # (Required) List of iSCSI interfaces.
      - name:                                       # (Required) Name of iSCSI interface (i.e. ib0, ib1).
        address:                                    # (Required) IPv4 address. Use the format 192.0.2.24.
        port:                                       # Interface iSCSI TCP listening port.
        opensm_configure:                           # Whether to configure OpenSM for port.
        opensm_subnet_prefix:                       # OpenSM subnet manager's subnet prefix.
        opensm_priority:                            # OpenSM subnet manager's priority.
        username:                                   # Storage target CHAP username.
        password:                                   # Storage target CHAP password.
        nr_sessions:                                # Interface number of sessions a target should connect.
        mtu:                                        # Interface maximum transmission unit measured in bytes.
        queue_depth:                                # Session queue depth.
        session_replacement_timeout:                # iSCSI session replacement timeout.
    eseries_ib_iser_username:                       # Default Storage target CHAP username (Default "").
    eseries_ib_iser_password:                       # Default Storage target CHAP password (Default "").
    eseries_ib_iser_nr_session:                     # Default number of sessions a target should connect (Default 1).
    eseries_ib_iser_mtu:                            # Default maximum transmission unit measured in bytes (Default 1500).
    eseries_ib_iser_queue_depth:                    # Default queue depth (Default 32).
    eseries_ib_iser_session_replacement_timeout:    # Default session replacement should a timeout occur (Default 20).
    eseries_ib_iser_opensm_configure:               # Default for whether to configure OpenSM. Default: true).
    eseries_ib_iser_opensm_subnet_prefix:           # Default OpenSM subnet manager's subnet prefix (Default: "0xfe80000000000000").
    eseries_ib_iser_opensm_subnet_priority:         # Default OpenSM subnet manager's priority (Default: 0).


iSCSI Variables (iscsi)
-----------------------
    eseries_common_group:                         # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
    eseries_iscsi_interfaces:                     # (Required) List of iSCSI interfaces.
      - name:                                     # (Required) Name of iSCSI interface (i.e. em1, ens160).
        address:                                  # (Required) IPv4 address. Use the format 192.0.2.24/24.
        port:                                     # Interface TCP port.
        nr_sessions:                              # Interface number of sessions a target should connect.
        mtu:                                      # Interface maximum transmission unit measured in bytes.
        username:                                 # Storage target CHAP username.
        password:                                 # Storage target CHAP password.
    eseries_iscsi_iqn:                            # Host IQN (iSCSI Qualified Name).
    eseries_iscsi_tcp_port:                       # iSCSI TCP port (Default: 3260).
    eseries_iscsi_nr_session:                     # Default number of sessions a target should connect (Default 1).
    eseries_iscsi_mtu:                            # Default maximum transmission unit measured in bytes (Default 1500).
    eseries_iscsi_username:                       # Default Storage target CHAP username (Default "").
    eseries_iscsi_password:                       # Default Storage target CHAP password (Default "").
    eseries_iscsi_queue_depth:                    # Default queue depth (Default 32).
    eseries_iscsi_session_replacement_timeout:    # Default session replacement should a timeout occur (Default 20).
    eseries_iscsi_node_settings:                  # Dictionary of values keyed by settings in iscsid.conf
    eseries_iscsi_configure_network:              # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
    eseries_iscsi_network_tool:                   # Configuration tool to defined network interfaces. Choices: ifupdown, netplan (Default: ifupdown)
    eseries_iscsi_refresh_sessions:               # Force all iSCSI sessions to be logout and login (Default: false).

Fibre Channel (fc)
------------------
    Not implemented

InfiniBand iSER (ib_iser)
-------------------------
    Not implemented

InfiniBand SRP (ib_srp)
-----------------------
    Not implemented

NVMe over Fibre Channel (nvme_fc)
---------------------------------
    Not implemented

NVMe over InfiniBand (nvme_ib)
------------------------------
    Not implemented

NVMe over RDMA over Converged Ethernet (nvme_roce)
--------------------------------------------------
    Not implemented

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
