netapp_eseries.host.tune_performance
=========

This package will configure system settings for maximum performance, possibly at the cost of increased energy usage.

This includes installing various packages/utilities needed to enable these settings, and disable/uninstall any services/packages that may conflict. 

Role Variables
--------------

### Required

None 

### Optional

* Force packages to upgrade in addition to ensuring they are installed (default: false).
  * `tune_performance_packages_upgrade: false`
* Specify if a custom netapp-eseries tuned role should be created/applied (default: true).
  * `tune_performance_configure_tuned: true`

For additional parameters see defaults/main.yml.