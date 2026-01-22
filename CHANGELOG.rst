=============================================
Netapp E-Series Host Collection Release Notes
=============================================

.. contents:: Topics


v2.0.1
======

Minor Changes
-------------

- Check for ifupdown in supported network management tools.


v2.0.0
======

Release Summary
---------------

This release focuses on improved code quality, compatibility with Ansible Core 2.19, and enhanced reliability for host
configuration and multipath handling.


Minor Changes
-------------

- Changed conditional checks to be explicit booleans for better code clarity and compatibility with Ansible Core 2.19.
- Increased the timeout for the `multipath -ll` command to accommodate large number of volumes.
- Updated the NetworkManager configuration to correct invalid interface profiles.
- Updated logic to auto-select the IP manager tool if multiple tools are installed.
- Ensured `/etc/iproute2` exists before configuring the routing table.
- Removed redundant parentheses and unnecessary wrapping quotes in conditionals.


v1.3.3
======

Release Summary
---------------

Minor updates


Minor Changes
-------------

- Update nvme_daemon.j2 to use udev rule to apply settings to NVMe device.
- Change eseries_multipath_command_timeout from 4 to 9 sec.


v1.3.2
======

Release Summary
---------------

Minor update to handle a change in default value of enable_foreign in multipath.conf


Minor Changes
-------------

- Update to handle a change in default value of enable_foreign in rhel 9 resulted in the NVMe volume not being detected
  by device mapper multipathing.


v1.3.0
======

Minor Changes
-------------

- Add rocky 8 support to netapp_eseries.host collection.
- netapp_eseries.host.ip - Add nmcli support for managing updating IP changes.
- netapp_eseries.host.ip - Add support for systemd-networkd hook dispatcher.
- netapp_eseries.host.ip - Add support for systemd-networkd in the 99-multihoming.j2 hook template.
- netapp_eseries.host.ip - Fix bug in the 99-multihoming.j2 hook template that causes the hook to fail when routes and rules were not defined.
- netapp_eseries.host.update_conf - Add timestamp to the update_conf module to avoid loosing previous changes by default.


v1.2.0
======

Release Summary
---------------

This release focused primarily on improving the code base for maintainability by relegating tasks to appropriate roles which significantly improved code reuse. While many of the role changes introduce improvements to inventory configuration options, backwards compatibility has been retained. Note that this release will now require Ansible 2.10 or later.


Minor Changes
-------------

- Require Ansible 2.10 or later.
- common - Remove the uninstall tags with the eseries_common_force_skip_uninstall variable and replace them with uninstall variables.
- common - Use ip command to rename interfaces rather than rebooting.
- ib - New base role to install and configure packages required for InfiniBand.
- ib - add support for configuring options for Mellanox HCAs.
- ib_iser - Remove ib_iser role's MTU default.
- ib_iser - Update to utilize iscsi role for all iSCSI specific tasks.
- ib_iser - add support for configuring options for Mellanox HCAs.
- ip - New base role to configure IP addresses, names, and implement hooks for network interfaces.
- ipoib - Replace ib_base dependency with new ip and ib roles.
- ipoib - add support for configuring options for Mellanox HCAs.
- iscsi - Improve configuration via role dictionaries to configure various iSCSI options.
- iscsi - Update to utilize the new ip base for all interface configurations.
- nar_santricity_common - Add common reboot tasks with a prompt when eseries_common_allow_host_reboot is false.
- nar_santricity_common - Add interface naming udev rule tasks.
- nvme - New base role to install and configure required packages for NVMe.
- nvme_ib - Update to utilize the new ib and nvme roles.
- nvme_ib - add support for configuring options for Mellanox HCAs.
- nvme_roce - Role to configure NVMe over RDMA over Converged Ethernet (RoCE) communications with NetApp E-Series storage systems.
- roce - Role to configure RDMA over Converged Ethernet (RoCE) communications with NetApp E-Series storage systems.
- selinux - Add role to configure SELinux.
- tune_performance - New role to apply performance configuration related to NetApp E-Series storage systems.
- update_conf - Add module for setting configuration files based on a dictionary.

Deprecated Features
-------------------

- ib_base - Did more than just configure InfiniBand (iSER, SRP, NVMe) so tasks have been logically grouped into other roles (ib, nvme, ib_iser, etc) to simplify and improve code maintainability.

Bugfixes
--------

- ib_opensm - Ensure opensm.service is started and it's validation task succeeds.
- nvme - Fix loading nvme-core with multipath=Y when previously loaded with multipath=N.

v1.1.0
======

Minor Changes
-------------

- common - Add common inventory structure and tasks to facilitate installing and configuring external packages.
- mount - Add eseries_mount_force_format flag to override the volume format protections.

Bugfixes
--------

- Fix netplan configuration template with embedded ib_iser variable.
- common - Fix SCSI bus recan operation when NVMe volumes are present.
- ib_iser - Fix target selection when non-IB iSER targets are present.
- ib_opensm - Ensure all opensm.conf* files are started and entered their expected state.
- ib_opensm - Fix systemd unit file to start up at the right time.
- iscsi - Fix target selection when non-iSCSI targets are present.
- multipath - Removed multipath driver conf files and updated dracut and update-initramfs commands to add multipath support.
- nvme_ib - Fix service and daemon to spin until NVMe sessions are established.
- nvme_ib - Fix systemd unit file so that the nvme_ib service starts a the right time.
- nvme_ib - Fix target selection when non-NVMe over IB targets are present.
- opensm - Workaround an apparent Ansible bug when trying to enable a systemd service that is enabled-runtime (https://github.com/ansible/ansible/issues/72451).

v1.0.1
======

Minor Changes
-------------

- Add eseries_common_force_skip_uninstall flag to avoid uninstall tasks when tags are inherited from the calling task.
- Allows all templates to be overwritten if additions need to be made locally.

Bugfixes
--------

- Fix persistence issue with ib_base kernel modules.

v1.0.0
======

Release Summary
---------------

1.0.0 release of ``netapp_eseries.host`` collection on 2021-03-31.

Minor Changes
-------------

- Add Fibre Channel support (fc).
- Add Infiniband SRP support (ib_srp).
- Add NVMe native support to multipath role.
- Add NVMe over Fibre Channel support (nvme_fc).
- Add NVMe over Infiniband role (nvme_ib).
- Add SAS support (sas).
- Add eseries_common_ignore_volumes list which forces volumes to be ignored.
- Add eseries_storage_setup_uninstall_multipath variable to skip uninstalling multipath.
- Add failure exception when there are not iSCSI interfaces or targets.
- Add multipath user_friendly_names support.
- Add namespace.name to modules for Ansible 2.10+ compliance.
- Remove dependency on logging to know NetApp E-Series volumes mapped/configured (eseries_mount_log).
- Remove hardcoded commands for scanning for volumes into protocol specific variables.
- Select single host to do volume related modifications (formatting) in case of hostgroup mapping.
- Separate IP over InfiniBand tasks into ipoib role.
- Separate OpenSM configuration tasks into opensm role.
- Separate all common InfiniBand tasks into ib_base role.
- Set the default format to ext4.
