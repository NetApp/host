netapp_eseries.host.mount
=========
Discover, format, and assign persistent mount point for NetApp E-Series mapped volumes on host.


Role Variables
--------------
eseries_common_group:                     # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
eseries_mount_volumes:                    # List of volumes to mount (Default: ["all_volumes"].
eseries_mount_format_type:                # Volume format type (Default: xfs)
eseries_mount_format_options:             # Volume format type options (Default: -d su=VOLUME_SEGMENT_SIZE_KBk,sw=VOLUME_STRIPE_COUNT -l version=2,su=VOLUME_SEGMENT_SIZE_KBk)
                                          #   VOLUME_SEGMENT_SIZE_KB will be replaced with the volume's segment size in kilobytes.
                                          #   VOLUME_STRIPE_COUNT will be replaced with the volume's RAID stripe count.
eseries_mount_persistent_mount_options:   # Volume mount options (Default: _netdev)
eseries_mount_root_directory:             # Volume mount path directory. (Default: /mnt/)


Tips
----
Add mount_to_hosts, format_type, format_options, mount_directory, mount_options to the volume's volume_metadata tags to provide information for mounting. This can be done with netapp_eseries.santricity.nar_santricity_host role. See inventory example below and SANtricity collection for more details.

    mount_to_hosts
    # Example inventory structure for E-Series storages system.
    eseries_storage_pool_configuration:
      - name: vg1
        raid_level: raid5
        criteria_drive_count: 3
        common_volume_configuration:
          volume_metadata:
            <place format and mounting variables here>    # This location will effect the whole storage pool
        volumes:
          - name: vg1
            host: ansible_hostname
            size: 10
            volume_metadata:
              <place format and mounting variables here>   # This location will only effect the volume itself)
          - name: vg2
            host: ansible_hostsgroup
            size: 10


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)
