netapp_eseries.host.common
=========
Collect information about E-Series storage systems and host-mapped volumes. 

    The following variables with be added to the runtime host inventory.
        storage_array_facts:    # Information from na_santricity_facts for eseries_common_group storage systems.
        eseries_volumes:        # Volume information for volumes mapped to the host. 

Variables
--------------
eseries_common_group:                     # (Required) Ansible host group or list of E-Series storage systems. (Default: eseries_storage_systems)
eseries_common_volume_workload_filter:    # Filters the volumes added to eseries_volumes.

Notes
----------
# Collect multiple variables containing uniquely filtered volume information.
Set common_volume_workload_filter to dynamically change the filter and then call the volume_facts.yml task directly. However, the gather_storage_facts.yml task must be call at least once to have the storage system information available to the task. If the host path for the volumes are required then call host_facts.yml task afterwards which will add it to the eseries_volumes variable. Use the set_fact module to storage eseries_volumes in a unique volumes. Lastly, repeat for each workload filter.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
