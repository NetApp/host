netapp_eseries.host.storage_setup
=================================
Setup multipath and required protocols for E-Series storage system on host.

Role Variables
--------------
eseries_common_group:                         # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
eseries_protocol:                             # Protocol to setup on host. Choices: auto, iscsi, fc, sas, ib_srp, ib_iser, nvme_ib, nvme_fc, nvme_roce (Default: auto).
eseries_storage_setup_uninstall_multipath:    # Whether to uninstall multipath when `eseries_storage_setup_uninstall==true` (Default: false).
eseries_storage_setup_uninstall:              # Whether to uninstall storage_setup role. (Default:  false)

Note
----
- The storage_setup role will call both the multipath and protocol roles.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)

