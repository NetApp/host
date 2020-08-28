netapp_eseries.host.ib_iser
=========
    Ensure InfiniBand iSER is configured on host.

Role Variables
--------------
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
eseries_ib_iser_username:                           # Default Storage target CHAP username (Default: "").
eseries_ib_iser_password:                           # Default Storage target CHAP password (Default: "").
eseries_ib_iser_nr_session:                         # Default number of sessions a target should connect (Default: 1).
eseries_ib_iser_mtu:                                # Default maximum transmission unit measured in bytes (Default: "").
eseries_ib_iser_queue_depth:                        # Default queue depth (Default: 32).
eseries_ib_iser_session_replacement_timeout:        # Default session replacement should a timeout occur (Default: 20).

eseries_ib_iser_opensm_configure:                   # Default for whether to configure OpenSM. Default: true).
eseries_ib_iser_opensm_subnet_prefix:               # Default OpenSM subnet manager's subnet prefix (Default: "0xfe80000000000000").
eseries_ib_iser_opensm_subnet_priority:             # Default OpenSM subnet manager's priority (Default: 0).

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)