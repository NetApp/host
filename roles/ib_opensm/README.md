netapp_eseries.host.ipoib
=========
    Configures OpenSM subnet manager.



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

General Notes
-------------
    - All InfiniBand networks requires at least one subnet manager to be running, even if there are now switches and your E-Series storage system is directly connected to the host.
    - In order to control multiple subnets on SLES and Ubuntu hosts, we've created a opensm.service and placed it in /etc/systemd/system/; this has the effect of overriding the default opensm.service service file.
    - When eseries_ib_opensm_subnet_manager_configure == True then all known InfiniBand interface ports will be configured even if one is not specified in eseries_ib_opensm_interfaces list.
    - A configuration file will be created for each subnet manager so the default opensm.conf file will never be used. Instead, opensm.conf.[0-9]* will be generated for each subnet manager in the default opensm path for your Linux operating system.

Variables
---------
eseries_ib_opensm_subnet_manager_configure:    # Default for whether to configure OpenSM (Default: false).
eseries_ib_opensm_subnet_prefix_base:          # Default OpenSM subnet manager's subnet prefix base. The last two digits will be determined by device port ordering (Default: "0xfe800000000000").
eseries_ib_opensm_subnet_priority:             # Default OpenSM subnet manager's priority. eseries_ib_iser_opensm_subnet_priority can be used instead (Default: 0). Choices: 0-15 (15 is highest priority).
eseries_ib_opensm_interfaces:                  # List of InfiniBand interfaces.
  - name:                                      # (Required) Use the name of InfiniBand interface (i.e. ib0, ib1) when IPoIB has been configured, otherwise use <DEVICE>_<PORT> (i.e. mlx5_0_1, mlx5_0_2)
    configure:                                 # Whether to configure OpenSM for port (Default: True).
    subnet_prefix:                             # OpenSM subnet manager's subnet prefix.
    priority:                                  # OpenSM subnet manager's priority.
eseries_ib_opensm_ubuntu_packages:             # Default package list for ubuntu (Default: opensm).
eseries_ib_opensm_suse_packages:               # Default package list for ubuntu (Default: opensm).
eseries_ib_opensm_rhel_packages:               # Default package list for ubuntu (Default: opensm).
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
