netapp_eseries.host.common
=========
Collect information about E-Series storage systems and host-mapped volumes,
and provide shared host setup helpers used by other roles such as package-manager repository controls.

    The following variables with be added to the runtime host inventory.
        storage_array_facts:    # Information from na_santricity_facts for eseries_common_group storage systems.
        eseries_volumes:        # Volume information for volumes mapped to the host. 

Variables
--------------
    eseries_common_group:                    # Inventory group containing E-Series storage systems (Default: eseries_storage_systems).
    eseries_common_volume_workload_filter:   # Filters the volumes added to eseries_volumes.
    eseries_common_allow_host_reboot:        # Whether reboots will allowed in an attempt to discover E-Series volumes.
    eseries_common_docker_host:              # Docker host for SANtricity Web Services Proxy.
    eseries_common_uninstall:                # Whether to uninstall all netapp_eseries.host roles included in playbook.
    eseries_common_allow_upgrades:           # Whether package upgrades are allowed when package-manager tasks run.
    eseries_common_skip_package_validation:  # Skip package validation checks when running package-manager tasks.
    eseries_common_package_group:            # Descriptive label for package-manager task output.
    eseries_common_existing_repos_disabled:   # Disable existing OS repositories before applying managed repos.
    eseries_common_yum_repos:                # Managed yum/dnf repository definitions.
    eseries_common_apt_repos:                # Managed apt repository definitions.

Note
----------
Define the package-manager variables above in inventory (group_vars or host_vars) when you want host.common to manage
repositories consistently across all targeted hosts. These variables are consumed by the package-manager task set that
now lives under the common role.

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
