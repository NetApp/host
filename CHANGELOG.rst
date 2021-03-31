=============================================
Netapp E-Series Host Collection Release Notes
=============================================

.. contents:: Topics


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
