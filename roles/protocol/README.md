netapp_eseries.host.protocol
=========
Setup up host for iSCSI, FC, SAS, InfiniBand SRP, InfiniBand iSER, NVMe over InfiniBand, NVMe over FC, or NVMe over RoCE.


Variables
--------------
eseries_protocol: auto                                # Protocol to setup on host. Choices: auto, iscsi, fc, sas, ib_srp, ib_iser, nvme_ib, nvme_fc, nvme_roce (Default: auto)
eseries_protocol_log_path: /var/log/                  # Host log path for protocols installed (Do not delete this file as its necessary for protocol removals).


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)
