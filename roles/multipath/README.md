netapp_eseries.host.multipath
=========
The role will install and configure multipath on a host.

Role Variables
--------------
eseries_multipath_configure_user_friendly_names:    # Whether to configure multipath to use the volume's name instead of the host WWID (Default: true).
eseries_multipath_path_selector:                    # Multipath path selector scheduler details (Default: "round-robin 0").
eseries_multipath_settle_timeout:                   # Seconds to wait for the udev queue to settle after multipathd starts, before rebuilding initramfs (Default: 30).
eseries_multipath_dracut_timeout:                   # Hard timeout in seconds for the dracut initramfs rebuild on RHEL/SUSE (Default: 600).
eseries_multipath_dracut_poll_interval:             # Polling interval in seconds while waiting for the dracut rebuild (Default: 5).

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)