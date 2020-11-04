netapp_eseries.host.ipoib
=========
    Configures OpenSM subnet manager for InfiniBand.



Example Playbook
----------------
- hosts: eseries_host_group
  collections:
    - netapp_eseries.host
  tasks:
    - name: Ensure Expected InfiniBand subnet managers are configured.
      import_role:
        name: ib_opensm


Example Inventory File
----------------------
ansible_host: 192.168.1.100
ansible_ssh_user: ssh_username
ansible_become_password: ssh_password
eseries_ib_opensm_subnet_manager_configure: true
eseries_ib_opensm_interfaces:
  - name: ib0
    address: 192.168.2.100/24
  - name: ib1
    address: 192.168.2.101/24

General Notes
-------------
    - All InfiniBand networks requires at least one subnet manager to be running, even if there are now switches and your E-Series storage system is directly connected to the host.
    - In order to control multiple subnets on Ubuntu hosts, we've created a unique systemd service named eseries_opensm.service that is configured to launch your specified subnet managers. DO NOT USE opensm.service.
    - When eseries_ib_opensm_subnet_manager_configure == True and eseries_ib_opensm_interfaces == [] then the OpenSM service will be enabled and configured to generically run on each InfiniBand interface. Use this configuration when directly connecting the host directly to your E-Series storage system.

Variables
---------
eseries_ib_opensm_interfaces:                  # List of InfiniBand interfaces.
  - name:                                      # (Required) Use the name of InfiniBand interface (i.e. ib0, ib1) when IPoIB has been configured, otherwise use <DEVICE>_<PORT> (i.e. mlx5_0_1, mlx5_0_2)
    configure:                                 # Whether to configure OpenSM for port (Default: True).
    subnet_prefix:                             # OpenSM subnet manager's subnet prefix.
    priority:                                  # OpenSM subnet manager's priority.
eseries_ib_opensm_subnet_manager_configure:            # Default for whether to configure OpenSM. eseries_ib_iser_opensm_configure can be used instead (Default: true).
eseries_ib_opensm_opensm_subnet_prefix:        # Default OpenSM subnet manager's subnet prefix. eseries_ib_iser_opensm_subnet_prefix can be used instead (Default: "0xfe80000000000000").
eseries_ib_opensm_opensm_subnet_priority:      # Default OpenSM subnet manager's priority. eseries_ib_iser_opensm_subnet_priority can be used instead (Default: 0). Choices: 0-15 (15 is highest priority).
eseries_ib_opensm_ubuntu_packages:             # Default packages for ubuntu (Default: [opensm]).
eseries_ib_opensm_suse_packages:               # Default packages for ubuntu (Default: [opensm]).
eseries_ib_opensm_rhel_packages:               # Default packages for ubuntu (Default: [opensm]).
eseries_ib_opensm_kernel_modules:              # Default loaded kernel modules (Default: [rdma_cm, mlx5_core, ib_ipoib]).
eseries_ib_opensm_log_path: /var/log/          # Default log path. Individual logs will be produced for each interface defined (opensm.conf.X.log); otherwise,
                                               #    all logging will be issued to opensm.log.

Uninstall
---------
To uninstall InfiniBand IPoIB, add '--tags ib_opensm_uninstall' to the ansible-playbook command.

    ansible-playbook -i inventory.yml playbook --tags ib_opensm_uninstall


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)
