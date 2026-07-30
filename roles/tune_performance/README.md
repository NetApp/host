netapp_eseries.host.tune_performance
=========

This package will configure system settings for maximum performance, possibly at the cost of increased energy usage.

This includes installing various packages/utilities needed to enable these settings, and disabling/uninstalling any services/packages that may override these settings, such as Ubuntu's ondemand.service which sets the CPU governor to ondemand or powersave.

Role Variables
--------------

### Required

None 

### Optional

* Force packages to upgrade in addition to ensuring they are installed (default: false).
  * `tune_performance_packages_upgrade: false`
* Specify if a custom netapp-eseries tuned role should be created/applied (default: true).
  * `tune_performance_configure_tuned: true`
  * Note this does not affect what packages are installed using the `tune_performance_packages_*` variable (which includes tuned by default). This allows users to use one of the default tuned roles or create their own if desired.

For additional parameters see defaults/main.yml.