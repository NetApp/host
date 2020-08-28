NetApp E-Series Host Collection
===============================
    NetApp E-Series Host collection consist of the latest available host utility roles relating to E-Series platforms.

    The roles in this collection can be used to configure your host storage connection for iSCSI, InfiniBand, and NVMe; Discover mapped E-Series volumes, format them to your specifications, and assign persistent mount points to them.

    Roles:
        - mount: Discover, format, and assign persistent mount points to your mapped E-Series volumes.

            This is the collection's main role since the mount role will, by default, include the multipath and protocol roles which calls the protocol roles themselves (iscsi, ib_iser, etc). The inventory variables eseries_mount_multipath_setup and eseries_mount_protocol_setup can be set to false avoid multipath and protocol configuration. However, the mount role's main functionality is to ensure that any mapped volumes are presented with persistent mounts on the host. This also means that if volumes are unmapped or removed, rerunning the role will remove them and clean up any mounting configuration.
            The mount role integrates with the SANtricity collection by utilizing the volume_metadata. Specify format_type, format_options, mount_dir, and/or mount_options in volume's metadata for the volume's mount and format details. The volumes name will be used as the mount directory.

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


Example Playbook
----------------
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


Other Useful Playbook tasks
---------------------------
    # Configure multipath Only
    - name: Install multipath on host.
      import_role:
        name: multipath

    # Configure the needed protocols Only.
    - name: Configure protocol on host.
      import_role:
        name: protocol

    # Mount all mapped volumes on host (Mounts will persist after reboot).
    - name: Just mount all volumes from hosts.
      import_role:
        name: mount

    # Temporarily unmount all mapped volumes from hosts.
    - name: Just unmount all volumes from hosts.
      import_role:
        name: unmount

    # Complete remove all mount.
    - name: Purge volumes from host and then delete the volumes from storage system.
      import_role:
        name: unmount
      vars:
        eseries_unmount_volumes: all_volumes             # List of volumes to sanitize. all_volumes will sanitize all volumes.
        eseries_unmount_wipe_format_signatures: false    # Whether to wipe format from storage.
        eseries_unmount_purge: false                     # Whether to purge volumes from host completely.
        eseries_unmount_unmap: false                     # Whether to unmap volumes to host on the storage system.
        eseries_unmount_delete: false                    # Whether to delete from storage system.


Important Notes
---------------
When taking advantage of the volume_metadata in the SANtricity collection's nar_santricity_host role, be sure that the host inventory does not conflict with volume_metadata entries. The volume's volume_metadata will take precedence over the host inventory!


Common Variables (common)
-------------------------
Note: Some variables may be repeated in other roles.
eseries_common_group:                               # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
eseries_common_volume_workload_filter:              # Filters the volumes added to eseries_volumes.


Mount Variables (mount)
--------------------
eseries_common_group: eseries_storage_systems       # Inventory group containing E-Series storage systems.


Multipath Variables (multipath)
-------------------------------


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


InfiniBand iSER Variables (ib_iser)
-----------------------------------
eseries_common_group:                               # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
eseries_iscsi_iqn:                                  # Host IQN (iSCSI Qualified Name).
eseries_ib_iser_interfaces:                         # (Required) List of iSCSI interfaces.
  - name:                                           # (Required) Name of iSCSI interface (i.e. ib0, ib1).
    address:                                        # (Required) IPv4 address. Use the format 192.0.2.24.
    port:                                           # Interface iSCSI TCP listening port.
    opensm_configure:                               # Whether to configure OpenSM for port.
    opensm_subnet_prefix:                           # OpenSM subnet manager's subnet prefix.
    opensm_priority:                                # OpenSM subnet manager's priority.
    username:                                       # Storage target CHAP username.
    password:                                       # Storage target CHAP password.
    nr_sessions:                                    # Interface number of sessions a target should connect.
    mtu:                                            # Interface maximum transmission unit measured in bytes.
    queue_depth:                                    # Session queue depth.
    session_replacement_timeout:                    # iSCSI session replacement timeout.
eseries_ib_iser_username:                           # Default Storage target CHAP username (Default "").
eseries_ib_iser_password:                           # Default Storage target CHAP password (Default "").
eseries_ib_iser_nr_session:                         # Default number of sessions a target should connect (Default 1).
eseries_ib_iser_mtu:                                # Default maximum transmission unit measured in bytes (Default 1500).
eseries_ib_iser_queue_depth:                        # Default queue depth (Default 32).
eseries_ib_iser_session_replacement_timeout:        # Default session replacement should a timeout occur (Default 20).
eseries_ib_iser_opensm_configure:                   # Default for whether to configure OpenSM. Default: true).
eseries_ib_iser_opensm_subnet_prefix:               # Default OpenSM subnet manager's subnet prefix (Default: "0xfe80000000000000").
eseries_ib_iser_opensm_subnet_priority:             # Default OpenSM subnet manager's priority (Default: 0).


iSCSI Variables (iscsi)
-----------------------
eseries_common_group:                               # Ansible host group or list of E-Series storage systems (Default: eseries_storage_systems).
eseries_iscsi_interfaces:                           # (Required) List of iSCSI interfaces.
  - name:                                           # (Required) Name of iSCSI interface (i.e. em1, ens160).
    address:                                        # (Required) IPv4 address. Use the format 192.0.2.24/24.
    port:                                           # Interface TCP port.
    nr_sessions:                                    # Interface number of sessions a target should connect.
    mtu:                                            # Interface maximum transmission unit measured in bytes.
    username:                                       # Storage target CHAP username.
    password:                                       # Storage target CHAP password.
eseries_iscsi_iqn:                                  # Host IQN (iSCSI Qualified Name).
eseries_iscsi_tcp_port:                             # iSCSI TCP port (Default: 3260).
eseries_iscsi_nr_session:                           # Default number of sessions a target should connect (Default 1).
eseries_iscsi_mtu:                                  # Default maximum transmission unit measured in bytes (Default 1500).
eseries_iscsi_username:                             # Default Storage target CHAP username (Default "").
eseries_iscsi_password:                             # Default Storage target CHAP password (Default "").
eseries_iscsi_queue_depth:                          # Default queue depth (Default 32).
eseries_iscsi_session_replacement_timeout:          # Default session replacement should a timeout occur (Default 20).
eseries_iscsi_node_settings:                        # Dictionary of values keyed by settings in iscsid.conf
eseries_iscsi_configure_network:                    # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
eseries_iscsi_network_tool:                         # Configuration tool to defined network interfaces. Choices: ifupdown, netplan (Default: ifupdown)
eseries_iscsi_refresh_sessions:                     # Force all iSCSI sessions to be logout and login (Default: false).


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)