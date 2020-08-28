netapp_eseries.host.unmount
=========
Unmount, wipe format metadata, and purge E-Series volume from host and unmapped or delete from NetApp E-Series storage.


Role Variables
--------------
eseries_common_group:                       # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
eseries_unmount_volumes:                   # (Required) E-Series volume name list to unmount (Default: []).
eseries_unmount_purge:                     # Purge volume completely from host (Default: false).
eseries_unmount_unmap:                     # Unmap E-Series volume from host (Default: false).
eseries_unmount_delete:                    # Delete E-Series volume from host (Default: false).
eseries_unmount_wipe_format_signatures:    # Clear the format signatures from the E-Series volume (Default: false)
eseries_mount_log_path:                     # Path for the eseries_mount_log which maintains volume mounting information (Default: /var/log/).


Notes
-----
- Unless otherwise specified volumes will only be temporarily unmounted from the host.
- Be aware that unmapping a host group volume will effect all hosts in the group. The E-Series host group itself will not be changed.
- Wipe format signatures to prevent format and data from being recovered in new volumes. E-Series IAF initialization only deletes the first and last 10mb of a newly created volume and ensuring parity in the rest of allocated storage block.


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)