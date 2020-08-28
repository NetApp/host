netapp_eseries.iscsi
=========


Role Variables
--------------
eseries_iscsi_node_settings:              # Dictionary of values keyed by settings in iscsid.conf
eseries_iscsi_interfaces:                 # List of iSCSI interfaces
  - name:                                 # Name of iSCSI interface (i.e. em1, ens160)
    address:                              # IPv4 address
    subnet:                               # IPv4 subnet mask
    subnet_cidr:                          # Ipv4 subnet mask in the CIDR formation (i.e. 192.168.1.0/24)
    gateway:                              # IPv4 gateway address
    mtu:                                  # Maximum transmission unit in bytes



eseries_iscsi_state_log_path:             # State log file path which records the actions performed by the mount role.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)