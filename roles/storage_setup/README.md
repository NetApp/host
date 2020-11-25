netapp_eseries.host.storage_setup
=================================
Setup multipath and required protocols for E-Series storage system on host.

Role Variables
--------------
eseries_common_group:                         # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
eseries_protocol:                             # Protocol to setup on host. Choices: auto, iscsi, fc, sas, ib_srp, ib_iser, nvme_ib, nvme_fc, nvme_roce (Default: auto).

Note
----
This will call both the multipath and protocol roles.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
