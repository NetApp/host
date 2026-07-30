netapp_eseries.host.srp
=========
    Configures InfiniBand SRP which installs and configure packages, kernel modules, and configures InfiniBand subnet manager if needed.

    * This role currently requires netapp_eseries.host.ib_base and has not been updated to utilize netapp_eseries.host.ib. As a result any node using netapp_eseries.host.ib_srp cannot be configured with any other netapp_eseries.host role depending on netapp_eseries.host.ib.

Role Variables
--------------
eseries_ib_srp_daemon_service:      # Path for the modified srp_daemon.service file (Default: /etc/systemd/system/srp_daemon.service).

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)