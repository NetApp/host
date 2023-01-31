<a name="netapp-e-series-host-collection"></a>
# NetApp E-Series Host Collection

NetApp E-Series Host collection consists of host utility roles relating to E-Series platforms.

The roles in this collection can be used to configure your host-storage connection for the different supported
protocols (e.g. iSCSI, iSER, NVMe over InfiniBand), discover the mapped E-Series volumes, format them to your
specifications, and assign persistent mount points to them.

<a name="table-of-contents"></a>
## Table of Contents

- [NetApp E-Series Host Collection](#netapp-e-series-host-collection)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
    - [Requirements for E-Series Storage Systems](#requirements-for-eseries-storage-systems)
    - [Requirements for E-Series Hosts](#requirements-for-e-series-hosts)
  - [Tested Ansible Versions](#tested-ansible-versions)
  - [Tested Platforms](#tested-platforms)
  - [Feature Roles](#feature-roles)
    - [Storage Setup](#storage-setup)
    - [Mount](#mount)
    - [Unmount](#unmount)
    - [Snapshot](#snapshot)
  - [Support Roles](#support-roles)
    - [Protocol](#protocol)
    - [Multipath](#multipath)
    - [SELinux](#selinux)
    - [IB OpenSM](#ib-opensm)
    - [IP over IB](#ip-over-ib)
    - [IB iSER](#ib-iser)
    - [IB srp](#ib-srp)
    - [NVMe over IB](#nvme-over-ib)
    - [NVMe over FC](#nvme-over-fc)
    - [NVMe over RoCE](#nvme-over-roce)
    - [RoCE](#roce)
    - [iSCSI](#iscsi)
    - [FC](#fc)
    - [SAS](#sas)
  - [License](#license)
  - [Maintainer Information](#maintainer-information)

<a name="requirements"></a>
## Requirements

<a name="requirements-for-eseries-storage-systems"></a>
### Requirements for E-Series Storage Systems

NetApp E-Series E2800 platform or newer (For older platforms, use NetApp E-Series SANtricity Web Services Proxy.)

<a name="requirements-for-e-series-hosts"></a>
### Requirements for E-Series Hosts.

- Python3.6 or later

<a name="tested-ansible-versions"></a>
## Tested Ansible Versions

Ansible 5.x (ansible-core 2.12)

<a name="tested-platforms"></a>
## Tested Platforms

- RHEL 8.4

<a name="feature-roles"></a>
## Feature Roles

Feature roles perform high level functions and will include the supporting roles as needed. Inventory variables will
need to be defined for any included feature roles as well as any needed [supporting roles](#support-roles). For
example, when the [Storage Setup](roles/storage_setup/README.md) role is included in your playbook and the targeted
E-Series storage system utilizes the NVMe over InfiniBand communication protocol then the
[NVMe over IB](roles/nvme_ib/README.md) role's inventory variables for will also need to be defined.

<a name="storage-setup"></a>
### Storage Setup

The storage_setup role installs and configures multipath and any supported protocols required for host-storage
communications based on E-Series mapped volumes. The support roles include multipath and protocol roles.

See [netapp_eseries.host.storage_setup documentation](roles/storage_setup/README.md) for more details.

<a name="mount"></a>
### Mount

The mount role will format and/or mount E-Series volumes on hosts. See
[netapp_eseries.host.mount documentation](roles/mount/README.md) for more details.

<a name="unmount"></a>
### Unmount

The unmount role will unmount E-Series volumes from hosts. See
[netapp_eseries.host.unmount documentation](roles/unmount/README.md) for more details.

<a name="snapshot"></a>
### Snapshot

The snapshot role attempts to create filesystem safe point-in-time snapshot images. See
[netapp_eseries.host.snapshot documentation](roles/snapshot/README.md) for more details.

<a name="support-roles"></a>
## Support Roles

Support Role are intended to aid the feature roles but may be called directly in unique situations.

<a name="protocol"></a>
### Protocol

The protocol role installs and configures any supported protocols required for host-storage communications based
on E-Series mapped volumes. See [netapp_eseries.host.protocol documentation](roles/protocol/README.md) for more
details.

<a name="multipath"></a>
### Multipath

The multipath role configures multipathing for SCSI and NVMe devices. See
[netapp_eseries.host.multipath documentation](roles/multipath/README.md) for more details.

<a name="selinux"></a>
### SELinux

The selinux role configures SELinux. See [netapp_eseries.host.selinux documentation](roles/selinux/README.md) for more
details.

<a name="ib-opensm"></a>
### IB OpenSM

The ib_opensm role configuration OpenSM subnet managers. See
[netapp_eseries.host.ib_opensm documentation](roles/ib_opensm/README.md) for more details.

<a name="ip-over-ib"></a>
### IP over IB

The ipoib role configures InfiniBand network interfaces. See
[netapp_eseries.host.ipoib documentation](roles/ipoib/README.md) for more details.

<a name="ib-iser"></a>
### IB iSER

The ib_iser role installs and configures the required kernel modules and packages for InfiniBand iSER protocol. See
[netapp_eseries.host.ib_iser documentation](roles/ib_iser/README.md) for more details.

<a name="ib-srp"></a>
### IB SRP

The ib_srp role installs and configures the required kernel modules and packages for InfiniBand SRP protocol. See
[netapp_eseries.host.ib_srp documentation](roles/ib_srp/README.md) for more details.

<a name="nvme-over-ib"></a>
### NVMe over IB

The nvme_ib role installs and configures the required kernel modules and packages for NVMe over InfiniBand protocol.
See [netapp_eseries.host.nvme_ib documentation](roles/nvme_ib/README.md) for more details.

<a name="#nvme-over-fc"></a>
### NVMe over FC

The nvme_fc role installs and configures the required kernel modules and packages for NVMe over Fibre Channel
protocol. See [netapp_eseries.host.nvme_fc documentation](roles/nvme_fc/README.md) for more details.

<a name="nvme-over-roce"></a>
### NVMe over RoCE

The nvme_roce role installs and configures the required kernel modules and packages for NVMe over RoCE protocol.
See [netapp_eseries.host.nvme_roce documentation](roles/nvme_roce/README.md) for more details.

<a name="roce"></a>
### RoCE

The RoCE role configures ethernet interfaces for the RoCE protocol (IB over Ethernet). See
[netapp_eseries.host.roce documentation](roles/roce/README.md) for more details.

<a name="iscsi"></a>
### iSCSI

The iscsi role installs and configures the required packages for the iSCSI protocol. See
[netapp_eseries.host.iscsi documentation](roles/iscsi/README.md) for more details.

<a name="fc"></a>
### FC

The fc role is simply a place holder for the fibre channel protocol. See
[netapp_eseries.host.fc documentation](roles/fc/README.md) for more details.

<a name="sas"></a>
### SAS

The sas role is simply a place holder for the SAS protocol. See
[netapp_eseries.host.sas documentation](roles/sas/README.md) for more details.

<a name="license"></a>
## License

BSD-3-Clause

<a name="maintainer-information"></a>
## Maintainer Information

- Nathan Swartz (@ndswartz)
- Joe McCormick (@iamjoemccormick)
