netapp_eseries.host.multipath
=========
The role will install and configure multipath on a host.

Role Variables
--------------
eseries_multipath_configure_user_friendly_names:    # Whether to configure multipath to use the volume's name instead of the host WWID (Default: true).
eseries_multipath_path_selector:                    # Multipath path selector scheduler details (Default: "round-robin 0").

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)