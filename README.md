NetApp E-Series Host Collection
===============================
    NetApp E-Series Host collection consist of the latest available host utility roles relating to E-Series platforms.

    The roles in this collection can be used to configure your host storage connection for iSCSI, InfiniBand, and NVMe; Discover mapped E-Series volumes, format them to your specifications, and assign persistent mount points to them.

    Roles:
        - storage_setup: Configures multipath and any required protocols for volumes mapped to host.
        - mount: Mounts all volumes mapped to host.
        - unmount: Unmounts E-Series volumes.
        - snapshot: Takes filesystem safe snapshots.
        - multipath: Configures multipath on host.
        - common: Collect storage system information, discover volumes on storage system, and spin up local docker web services proxy instance.
        - protocol: Determines and configures host-storage system protocol communications.
        - fc: Configures fibre channel protocol communications (nothing to do)
        - ib_base: Configures common InfiniBand configurations.
        - ib_iser: Configures host-storage system communications for the InfiniBand iSER protocol.
        - ib_opensm: Configures OpenSM on host.
        - ib_srp: Configures host-storage system communications for the InfiniBand SRP protocol.
        - ipoib: Configures IP over InfiniBand on host.
        - iscsi: Configures host-storage system communications for the iSCSI protoc0l.
        - nvme_fc: Configures host-storage system communications for the NVMe over fibre channel protocol.
        - nvme_ib: Configures host-storage system communications for the NVMe over Infiniband protocol.
        - nvme_roce: Not implemented yet
        - sas: Configures SAS communications (nothing to do)

    Tested Platforms:
        - RHEL 7.7
        - SLES 12sp4
        - Ubuntu 16.04 LTS
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
    - When taking advantage of the volume_metadata in the SANtricity collection's nar_santricity_host role, be sure that the host inventory does not conflict with volume_metadata entries. The volume's volume_metadata will take precedence over the host inventory!
    - Set `eseries_common_force_skip_uninstall==True` when importing this collection's role(s) into your playbook/role that use tags to avoid inadvertently applying tags to uninstall tasks.

*Note: Some variables may be repeated in multiple roles which is done to maintain continuity between roles should the defaults be overwritten.
Common Variables (common)
-------------------------
    eseries_common_group:                              # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
    eseries_common_volume_workload_filter:             # Filters the volumes added to eseries_volumes.
    eseries_common_allow_host_reboot:                  # Whether reboots will allowed in an attempt to discover E-Series volumes. (Default: false)
    eseries_common_docker_host:                        # Docker host for SANtricity Web Services Proxy. (Default: unix://var/run/docker.sock)
    eseries_common_force_skip_uninstall:               # Forces to skip uninstallation when roles has been called dynamically with applied tags; otherwise the
                                                       #   applied tags are also applied to uninstallation (Default: False).
Multipath Variables (multipath)
-------------------------------
    eseries_multipath_configure_user_friendly_names:   # Ensures that all volumes are presented with their given name. (Default: true)
    eseries_multipath_conf_d_path:                     # The directory path for E-Series specific wwid-alias definitions (Default: /etc/multipath/conf.d/).
    eseries_multipath_kernel_modules:                  # Kernel modules that need to be loaded in order for multipath to be functioning correctly. (Default [dm_multipath])

Protocol Variables (protocol)
-----------------------------
    eseries_protocol:             # Protocols to install which are determined by the storage systems that have mapped volumes. `auto` will
                                  #   determine which protocols are required.
                                  #   Choices: auto, fc, ib_iser, ib_srp, iscsi, nvme_fc, nvme_ib, nvme_roce, sas (Default: auto)
    eseries_protocol_log_path:    # Path to eseries_protocol_log which is used to maintain a record of communication protocols installed. (Default: /var/log/)

Storage_Setup Variables
-----------------------
    eseries_multipath_configure_user_friendly_names:   # Ensures that all volumes are presented with their given name. (Default: true)
    eseries_multipath_conf_d_path:                     # The directory path for E-Series specific wwid-alias definitions. (Default: /etc/multipath/conf.d/)
    eseries_multipath_kernel_modules:                  # Kernel modules that need to be loaded in order for multipath to be functioning correctly. (Default [dm_multipath])
    eseries_protocol:                                  # Protocols to install which are determined by the storage systems that have mapped volumes. `auto` will
                                                       #   determine which protocols are required.
                                                       #   Choices: auto, fc, ib_iser, ib_srp, iscsi, nvme_fc, nvme_ib, nvme_roce, sas (Default: auto)

Mount Variables (mount)
--------------------
    * Note: `VOLUME_SEGMENT_SIZE_KB` and `VOLUME_STRIPE_COUNT` will be replaced with the correct values from your E-Series storage system.
    eseries_mount_volumes:                        # List of volume names to mount. `all_volumes` ensures all mapped volumes are mounted. (Default:["all_volumes"])
    eseries_mount_format_type:                    # Volume format type. (Default: xfs)
    eseries_mount_format_options:                 # Volume format options. (Default: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk")
    eseries_mount_persistent_mount_options:       # Volume mount options. (Default: "_netdev")
    eseries_mount_root_directory:                 # Volume mount directory. (Default: /mnt/)
    eseries_mount_skip_unmount:                   # Whether to skip mounting volumes. (Default: false)
    eseries_mount_format_type_options:            # Mount options for different formats. Used when eseries_mount_format_options is not defined.
                                                  # Defaults: xfs: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk"
                                                  #           ext4: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk"
                                                  #           btrfs: "-d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk"

    *Tip: Add mount_to_hosts, format_type, format_options, mount_dir, mount_options to the volume's volume_metadata tags to provide information for mounting. This can be done with netapp_eseries.santricity.nar_santricity_host role. See SANtricity collection for more details.

Unmount Variables (unmount)
---------------------------
    eseries_common_group:                         # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
    eseries_unmount_volumes:                      # (Required) E-Series volume name list to unmount (Default: []).
    eseries_unmount_purge:                        # Purge volume completely from host (Default: false).
    eseries_unmount_unmap:                        # Unmap E-Series volume from host (Default: false).
    eseries_unmount_delete:                       # Delete E-Series volume from host (Default: false).
    eseries_unmount_wipe_format_signatures:       # Clear the format signatures from the E-Series volume (Default: false)

Snapshot Variables (snapshot)
-----------------------------
    eseries_snapshot_pit_safe:            # Whether to wait for all files to be close, sync and unmount volume before taking a point-in-time snapshot (Default: True)
                                          #   image; otherwise, a simple filesystem suspend (dmsetup suspend) will be issued (Default: True).
    eseries_snapshot_pit_timeout_sec:     # Maximum time to wait for files to closes when I(eseries_snapshot_pits_safe==True) (Default: 600).
    eseries_snapshot_pits:                # List of consistency group point-in-time snapshot definitions.
      - group_name:                       # Snapshot consistency group name.
        pit_name:                         # (Optional) Name for the point-in-time snapshot.
        pit_description:                  # (Optional) Description for the point-in-time snapshot.
        volumes:                          # (Optional) List of volumes that are a subset of the consistency group's volume members.


InfiniBand Base Variables (ib_base)
-----------------------------------
    eseries_ib_base_ipoib_enabled:                # Whether InfiniBand IPoIB should be configured (Default: false).
    eseries_ib_base_iser_enabled:                 # Whether InfiniBand iSER should be configured (Default: false).
    eseries_ib_base_srp_enabled:                  # Whether InfiniBand SRP should be configured (Default: false).
    eseries_ib_base_rdma:                         # Directory for RDMA configuration files (Default: /etc/rdma/).
    eseries_ib_base_rdma_memory_conf:             # Absolute path to the rdma.conf file for configuring rdma security limitations (Default: /etc/security/limits.d/rdma.conf).
    eseries_ib_base_modules_d:                    # Systemd module configuration files directory (Default: file/etc/modules-load.d/).
    eseries_ib_base_ubuntu_packages:              # Packages to install for hosts running Ubuntu (Default: [infiniband-diags, rdma-core]).
    eseries_ib_base_suse_packages:                # Packages to install for hosts running SUSE (Default: [infiniband-diags, rdma-core]).
    eseries_ib_base_rhel_packages:                # Packages to install for hosts running RedHat (Default: [infiniband-diags, rdma-core]).
    eseries_ib_base_kernel_modules:               # InfiniBand base kernel modules (Default: [ib_core, ib_umad, ib_uverbs, rdma_cm, rdma_ucm, mlx5_core, mlx5_ib])
    eseries_ib_base_ipoib_kernel_modules:         # InfiniBand base kernel modules for InfiniBand IPoIB (Default: [ib_ipoib]).
    eseries_ib_base_srp_kernel_modules:           # InfiniBand base kernel modules for InfiniBand SRP (Default: [ib_srp]).
    eseries_ib_base_iser_kernel_modules:          # InfiniBand base kernel modules for InfiniBand iSER (Default: [ib_ipoib, ib_iser]).

InfiniBand OpenSM Variables (ib_opensm)
---------------------------------------
    eseries_ib_opensm_subnet_manager_configure:   # Default for whether to configure OpenSM (Default: false).
    eseries_ib_opensm_subnet_prefix_base:         # Default OpenSM subnet manager's subnet prefix base. The last two digits will be determined by device port ordering (Default: "0xfe800000000000").
    eseries_ib_opensm_subnet_priority:            # Default OpenSM subnet manager's priority. eseries_ib_iser_opensm_subnet_priority can be used instead (Default: 0). Choices: 0-15 (15 is highest priority).
    eseries_ib_opensm_interfaces:                 # List of InfiniBand interfaces.
      - name:                                     # (Required) Use the name of InfiniBand interface (i.e. ib0, ib1) when IPoIB has been configured, otherwise use <DEVICE>_<PORT> (i.e. mlx5_0_1, mlx5_0_2)
        configure:                                # Whether to configure OpenSM for port (Default: True).
        subnet_prefix:                            # OpenSM subnet manager's subnet prefix.
        priority:                                 # OpenSM subnet manager's priority.
    eseries_ib_opensm_ubuntu_packages:            # Default package list for ubuntu (Default: opensm).
    eseries_ib_opensm_suse_packages:              # Default package list for ubuntu (Default: opensm).
    eseries_ib_opensm_rhel_packages:              # Default package list for ubuntu (Default: opensm).
    eseries_ib_opensm_kernel_modules:             # Default loaded kernel modules (Default: [rdma_cm, mlx5_core, ib_ipoib]).
    eseries_ib_opensm_log_path: /var/log/         # Default log path. Individual logs will be produced for each interface defined (opensm.conf.X.log); otherwise,
                                                  #    all logging will be issued to opensm.log.

IP over InfiniBand Variables (ipoib)
------------------------------------
    eseries_ipoib_interfaces:                     # (Required) List of InfiniBand interfaces (Note: Not required if eseries_ib_iser_interfaces is defined).
      - name:                                     # (Required) Name of InfiniBand interface (i.e. ib0, ib1).
        address:                                  # (Required) IPv4 address. Use the format 192.0.2.24.
        mtu:                                      # Interface maximum transmission unit measured in bytes.
    eseries_ipoib_mtu:                            # Default maximum transmission unit measured in bytes (Default: "").
    eseries_ipoib_kernel_modules:                 # Default loaded kernel modules (Default: [rdma_cm, mlx5_core, ib_ipoib]).

InfiniBand iSER Variables (ib_iser)
-----------------------------------
    eseries_iscsi_iqn:                            # Host IQN (iSCSI Qualified Name).
    eseries_ib_iser_interfaces:                   # (Required) List of iSCSI interfaces.
      - name:                                     # (Required) Name of iSCSI interface (i.e. ib0, ib1).
        address:                                  # (Required) IPv4 address. Use the format 192.0.2.24.
        port:                                     # Interface iSCSI TCP listening port.
        username:                                 # Storage target CHAP username.
        password:                                 # Storage target CHAP password.
        nr_sessions:                              # Interface number of sessions a target should connect.
        mtu:                                      # Interface maximum transmission unit measured in bytes.
        queue_depth:                              # Session queue depth.
        session_replacement_timeout:              # iSCSI session replacement timeout.
        configure:                                # Whether to configure OpenSM for interface.
        subnet_prefix:                            # OpenSM subnet manager's subnet prefix.
        priority:                                 # OpenSM subnet manager's priority.
    eseries_ib_iser_username:                     # Default Storage target CHAP username (Default: "").
    eseries_ib_iser_password:                     # Default Storage target CHAP password (Default: "").
    eseries_ib_iser_nr_session:                   # Default number of sessions a target should connect (Default: 1).
    eseries_ib_iser_mtu:                          # Default maximum transmission unit measured in bytes (Default: "").
    eseries_ib_iser_queue_depth:                  # Default queue depth (Default: 32).
    eseries_ib_iser_session_replacement_timeout:  # Default session replacement should a timeout occur (Default: 20).

InfiniBand SRP Variables (ib_srp)
---------------------------------
    eseries_ib_srp_daemon_service:                # Path for the modified srp_daemon.service file (Default: /etc/systemd/system/srp_daemon.service).
    eseries_ib_srp_ubuntu_packages:               # Required Ubuntu packages (Default: srptools).
    eseries_ib_srp_suse_packages:                 # Required SUSE packages (Default: srptools).
    eseries_ib_srp_rhel_packages:                 # Required RedHat packages (Default: srptools).

iSCSI Variables (iscsi)
-----------------------
    eseries_common_group:                         # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
    eseries_iscsi_configure_network:              # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
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
    eseries_iscsi_refresh_sessions:               # Force all iSCSI sessions to be logout and login (Default: false).
    eseries_iscsi_ubuntu_packages:                # iSCSI packages for Ubuntu (Default: [open-iscsi]).
    eseries_iscsi_suse_packages:                  # iSCSI packages for SUSE (Default: [open-iscsi]).
    eseries_iscsi_rhel_packages:                  # iSCSI packages for RedHat (Default: [iscsi-initiator-utils]).

Fibre Channel (fc)
------------------
    None

InfiniBand iSER (ib_iser)
-------------------------
    eseries_iscsi_iqn:                              # Host IQN (iSCSI Qualified Name).
    eseries_ib_iser_interfaces:                     # (Required) List of iSCSI interfaces.
      - name:                                       # (Required) Name of iSCSI interface (i.e. ib0, ib1).
        address:                                    # (Required) IPv4 address. Use the format 192.0.2.24.
        port:                                       # Interface iSCSI TCP listening port.
        username:                                   # Storage target CHAP username.
        password:                                   # Storage target CHAP password.
        nr_sessions:                                # Interface number of sessions a target should connect.
        mtu:                                        # Interface maximum transmission unit measured in bytes.
        queue_depth:                                # Session queue depth.
        session_replacement_timeout:                # iSCSI session replacement timeout.
        configure:                                  # Whether to configure OpenSM for interface.
        subnet_prefix:                              # OpenSM subnet manager's subnet prefix.
        priority:                                   # OpenSM subnet manager's priority.
    eseries_ib_iser_username:                       # Default Storage target CHAP username (Default: "").
    eseries_ib_iser_password:                       # Default Storage target CHAP password (Default: "").
    eseries_ib_iser_nr_session:                     # Default number of sessions a target should connect (Default: 1).
    eseries_ib_iser_mtu:                            # Default maximum transmission unit measured in bytes (Default: "").
    eseries_ib_iser_queue_depth:                    # Default queue depth (Default: 32).
    eseries_ib_iser_session_replacement_timeout:    # Default session replacement should a timeout occur (Default: 20).

InfiniBand SRP (ib_srp)
-----------------------
    eseries_ib_srp_daemon_service:                  # Path for the modified srp_daemon.service file (Default: /etc/systemd/system/srp_daemon.service).

NVMe over Fibre Channel (nvme_fc)
---------------------------------
    eseries_nvme_fc_use_nvmefc_boot_connections:    # Whether to nvmefc-boot-connections.service when available. Note, nvmefc_boot_connections
                                                    #   is not available with all versions of nvme-cli and sometimes will require a host reboot (Default: False)
    eseries_nvme_fc_service_name:                   # Name of NVMe-FC connection service (Default: eseries_nvme_fc.service).
    eseries_nvme_fc_queue_depth:                    # Overrides the default number of elements in the I/O queues created by the driver (Default: 1024).
    eseries_nvme_fc_controller_loss_timeout:        # Overrides the default controller loss timeout period in seconds (Default: 3600).
    eseries_nvme_fc_modules:                        # The following modules will be added to /etc/modprobe.d/eseries_nvme_fc.conf. Whatever Linux FC driver is
                                                    #    used needs to have nvme enabled.
      - name: lpfc                                  # Emulex/Broadcom driver (if driver not present the modprobe option will just fail)
        parameters: lpfc_enable_fc4_type=3          #   3 enables both NVMe and SCSI
      - name: qla2xxx                               # QLogic driver (if driver not present the modprobe option will just fail)
        parameters: ql2xnvmeenable=1                #   1 enables both NVMe and SCSI

NVMe over InfiniBand (nvme_ib)
------------------------------
    eseries_nvme_nqn:                                   # Host NQN. When not specified, nqn will be derived from host.
    eseries_nvme_ib_interfaces:                         # (Required) List of NVMe InfiniBand interfaces.
      - name:                                           # (Required) Name of NVMe InfiniBand  interface (i.e. ib0, ib1).
        address:                                        # (Required) IPv4 address. Use CIDR form (ex. 192.168.1.1/24).
        port:                                           # Interface NVMe IPoIB listening port.
        mtu:                                            # Interface maximum transmission unit measured in bytes.
        queue_depth:                                    # Session queue depth.
        configure:                                      # Whether to configure OpenSM for interface.
        subnet_prefix:                                  # OpenSM subnet manager's subnet prefix.
        priority:                                       # OpenSM subnet manager's priority.

    eseries_nvme_ib_username:                           # Default Storage target CHAP username (Default: "").
    eseries_nvme_ib_password:                           # Default Storage target CHAP password (Default: "").
    eseries_nvme_ib_mtu:                                # Default maximum transmission unit measured in bytes (Default: "").
    eseries_nvme_ib_queue_depth:                        # Default queue depth (Default: 32).
    eseries_nvme_ib_session_replacement_timeout:        # Default session replacement should a timeout occur (Default: 20).
    eseries_nvme_ib_service_name:                       # Custom NVMe over InfiniBand systemd service name (Default: eseries_nvme_ib.service).

NVMe over RDMA over Converged Ethernet (nvme_roce)
--------------------------------------------------
    Not implemented

SAS (sas)
---------
    None

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
