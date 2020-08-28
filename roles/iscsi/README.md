netapp_eseries.host.iscsi
=========


Role Variables
--------------
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

Notes
-----
WARNING! Role will configure the specified iSCSI network interfaces unless eseries_iscsi_configure_network is set to false.
WARNING! Role will utilize ifupdown tool unless otherwise specified. Currently, ifupdate is the only implemented configuration tool. 

Note: Reduction in session will only be configured but not applied.
License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)