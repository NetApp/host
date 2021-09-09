netapp_eseries.host.ipoib
=========
    Configures IP over InfiniBand which installs and configure packages, kernel modules, and configures network interfaces using either ifupdown or netplan.

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
eseries_ipoib_configure_network            # Whether to configure networking interfaces (Default: true)
eseries_ipoib_mtu:                         # Default maximum transmission unit measured in bytes (Default: "").
eseries_ipoib_interfaces:                  # (Required) List of InfiniBand interfaces (Note: Not required if eseries_ib_iser_interfaces is defined).
  - name:                                  # (Required) Name of InfiniBand interface (i.e. ib0, ib1).
    address:                               # (Required) IPv4 address. Use the format 192.0.2.24.
    mtu:                                   # Interface maximum transmission unit measured in bytes.
eseries_connected_mode:                    # Enables connected mode on all interfaces. Note that this is not supported after ConnectX-4 devices
                                           #    and some newer Linux distributions do not support it (Default: false).

Uninstall
---------
To uninstall InfiniBand IPoIB, add '--tags ipoib_uninstall' to the ansible-playbook command.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
