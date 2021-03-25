netapp_eseries.host.snapshot
=========
This role attempts to create filesystem safe point-in-time snapshot images. It will ensures file handles are closed, cache is flushed, I/O is completed, and the base volume is temporarily unmounted. Once unmounted, a snapshot will be generated and the volume remounted.

See netapp_eseries.santricity collection's readme for details on how to create, use, and maintain snapshot consistency groups. The collection's role, nar_santricity_host,

WARNING! This role cannot be application aware and will require applications to be placed into a filesystem consistent state prior to execution; also be aware of  any high-availability solutions that will attempt to remount unmounted devices such as the NetApp E-Series BeeGFS HA solution.

Role Variables
--------------
eseries_snapshot_pit_safe: true       # Whether to wait for all files to be close, sync and unmount volume before taking a point-in-time snapshot
                                      #   image; otherwise, a simple filesystem suspend (dmsetup suspend) will be issued (Default: True).
eseries_snapshot_pit_timeout_sec:     # Maximum time to wait for files to closes when I(eseries_snapshot_pits_safe==True) (Default: 600).
eseries_snapshot_pits:                # List of consistency group point-in-time snapshot definitions.
  - group_name:                       # Snapshot consistency group name
    pit_name:                         # (Optional) Name for the point-in-time snapshot.
    pit_description:                  # (Optional) Description for the point-in-time snapshot.
    volumes:                          # (Optional) List of volumes that are a subset of the consistency group's volume members.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
