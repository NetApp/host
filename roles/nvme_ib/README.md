netapp_eseries.host.nvme_ib
=========
    Ensure InfiniBand iSER is configured on host.

Role Variables
--------------
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

General Notes
-------------
A customized systemd service daemon will be generated based on the required targets needed for existing storage system mappings. You can view the generated daemon at /etc/nvme/eseries_nvme_ib_daemon. The daemon is controlled with the systemd service eseries_nvme_ib.service which will ensure connectivity during boot.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)