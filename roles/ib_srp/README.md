netapp_eseries.host.srp
=========
    Configures InfiniBand SRP which installs and configure packages, kernel modules, and configures InfiniBand subnet manager if needed.

Role Variables
--------------
eseries_ib_srp_daemon_service:      # Path for the modified srp_daemon.service file (Default: /etc/systemd/system/srp_daemon.service).
eseries_ib_srp_ubuntu_packages:     # Required Ubuntu packages (Default: srptools).
eseries_ib_srp_suse_packages:       # Required SUSE packages (Default: srptools).
eseries_ib_srp_rhel_packages:       # Required RedHat packages (Default: srptools).

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)