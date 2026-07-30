# netapp_eseries.host.nvme_fc
    Ensure NVMe over Fibre Channel is configured on host.

## Role Variables
    eseries_nvme_fc_use_nvmefc_boot_connections:    # Whether to nvmefc-boot-connections.service when available. Note, nvmefc_boot_connections
                                                    #   is not available with all versions of nvme-cli and sometimes will require a host reboot (Default: False)
    eseries_nvme_fc_service_name:                   # Name of NVMe-FC connection service (Default: eseries_nvme_fc.service).
    eseries_nvme_fc_queue_depth:                    # Overrides the default number of elements in the I/O queues created by the driver (Default: 1024).
    eseries_nvme_fc_controller_loss_timeout:        # Overrides the default controller loss timeout period in seconds (Default: 3600).
    eseries_nvme_fc_modules:                        # The following modules will be added to /etc/modprobe.d/eseries_nvme_fc.conf. Whatever Linux FC driver is
                                                    #    used needs to have nvme enabled.
      - name: lpfc                                  # Emulex/Broadcom driver (if driver not present the modprobe option will just fail)
        parameters: lpfc_enable_fc4_type=3          #   3 enables both NVMe and SCSI
      - name: qla2xxx                               # QLogic driver (if driver not present the modprobe option will just fail)
        parameters: ql2xnvmeenable=1                #   1 enables both NVMe and SCSI
    eseries_nvme_fc_uninstall:                      # Whether to uninstall nvme_fc role. (Default: false)

## General Notes
    It is recommended to call netapp_eseries.host.storage_setup instead of calling supporting roles directly
    which will configure all related protocols based on storage mapped to the targeted host. However, if you
    need to call this role directly, be sure to set the include_role public option to true. This is important
    to ensure role defaults are available when passed to other supporting roles. All defaults are prefixed with
    eseries_nvme_fc_* to prevent variable conflicts with other roles.

    - name: Ensure NVMe over Fibre Channel protocol has been setup
      ansible.builtin.include_role:
        name: netapp_eseries.host.nvme_fc
        public: true

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
