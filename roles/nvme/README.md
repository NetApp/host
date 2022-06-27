# netapp_eseries.host.nvme
    Install and configure required packages for NVMe.

## Role Variables
    eseries_nvme_nqn:                       # NVMe qualified name (NQN). Setting this will update the host's NQN.
    eseries_nvme_port:                      # NVMe port to use
    eseries_nvme_queue_depth:               # I/O queue depth
    eseries_nvme_controller_loss_timeout:   # Seconds before considering a controller lost.
    eseries_nvme_uninstall:               # Whether to uninstall the nvme role. (Default: false)

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)
