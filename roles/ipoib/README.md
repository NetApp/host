netapp_eseries.host.ipoib
=========
    Configures IP over InfiniBand which installs and configure packages, kernel modules, configures network interfaces (ifupdown or netplan), and configures InfiniBand subnet manager if needed.


Example Playbook
----------------
- hosts: eseries_host_group
  collections:
    - netapp_eseries.host
  tasks:
    - name: Ensure multipath and expected protocols are installed and configured. Format and configure persistent mounts for any volumes mapped to the host.
      import_role:
        name: ipoib


Example Inventory File
----------------------
ansible_host: 192.168.1.100
ansible_ssh_user: ssh_username
ansible_become_password: ssh_password
eseries_ipoib_opensm_configure: true
eseries_ipoib_interfaces:
  - name: ib0
    address: 192.168.2.100/24
  - name: ib1
    address: 192.168.2.101/24


Variables
---------
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
eseries_ipoib_opensm_subnet_priority:      # Default OpenSM subnet manager's priority. eseries_ib_iser_opensm_subnet_priority can be used instead (Default: 1). Choices: 1-15 (15 is highest).
eseries_ipoib_ubuntu_packages:             # Default packages for ubuntu (Default: [rdma-core, infiniband-diags]).
eseries_ipoib_suse_packages:               # Default packages for ubuntu (Default: [rdma-core, infiniband-diags]).
eseries_ipoib_rhel_packages:               # Default packages for ubuntu (Default: [rdma-core, infiniband-diags]).
eseries_ipoib_kernel_modules:              # Default loaded kernel modules (Default: [rdma_cm, mlx5_core, ib_ipoib]).
eseries_ipoib_uninstall_kernel_modules:    # Default unloaded kernel modules when uninstalled. (Default: [mlx5_ib, mlx5_core, ib_ipoib])


Notes
-----
If using connectX-3 or earlier, override eseries_ipoib_kernel_modules and eseries_ipoib_uninstall_kernel_modules defaults in your inventory to use mlx4.


Uninstall
---------
To uninstall InfiniBand IPoIB, add '--tags ipoib_uninstall' to the ansible-playbook command.

    Note: Only kernel modules mlx5_ib, mlx5_core, and ib_ipoib will be unloaded.


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)
