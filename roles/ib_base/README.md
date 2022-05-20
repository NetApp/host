netapp_eseries.host.ib_base
=========
    Install and configure base packages for InfiniBand.

    * Note that this role has been deprecated and will be removed in a future release. Please update to use the netapp_eseries.host.ib and netapp_eseries.host.nvme roles instead.
    * Do not configure any nodes with both netapp_eseries.host.ib_base and netapp_eseries.host.ib roles.

Variables (Values specified are the defaults)
---------
eseries_ib_base_skip:                    # Whether we should skip configuring InfiniBand entirely (Default: false). Useful to just use functionality provided by other roles that inherit this one when IB is already setup.
eseries_ib_base_ipoib_enabled:           # Whether InfiniBand IPoIB should be configured (Default: false).
eseries_ib_base_iser_enabled:            # Whether InfiniBand iSER should be configured (Default: false).
eseries_ib_base_srp_enabled:             # Whether InfiniBand SRP should be configured (Default: false).
eseries_ib_base_nvme_enabled:            # Whether InfiniBand SRP should be configured (Default: false).
eseries_ib_base_rdma:                    # Directory for RDMA configuration files (Default: /etc/rdma/).
eseries_ib_base_rdma_memory_conf:        # Absolute path to the rdma.conf file for configuring rdma security limitations (Default: /etc/security/limits.d/rdma.conf).
eseries_ib_base_modules_load_d:          # File directory for required kernel modules (Default: /etc/modules-load.d/).
eseries_ib_base_modules_d:               # File directory for the default options for required kernel modules (Default: /etc/modules.d/).
eseries_ib_base_ubuntu_packages:         # Packages to install for hosts running Ubuntu (Default: [infiniband-diags, rdma-core]).
eseries_ib_base_suse_packages:           # Packages to install for hosts running SUSE (Default: [infiniband-diags, rdma-core]).
eseries_ib_base_rhel_packages:           # Packages to install for hosts running RedHat (Default: [infiniband-diags, rdma-core]).
eseries_ib_base_kernel_modules:          # InfiniBand base kernel modules (Default: [ib_core, ib_umad, ib_uverbs, rdma_cm, rdma_ucm, mlx5_core, mlx5_ib])
eseries_ib_base_ipoib_kernel_modules:    # InfiniBand base kernel modules for InfiniBand IPoIB (Default: [ib_ipoib]).
eseries_ib_base_srp_kernel_modules:      # InfiniBand base kernel modules for InfiniBand SRP (Default: [ib_srp]).
eseries_ib_base_iser_kernel_modules:     # InfiniBand base kernel modules for InfiniBand iSER (Default: [ib_ipoib, ib_iser]).
eseries_ib_base_nvme_kernel_modules      # InfiniBand base kernel modules for NVMe over InfiniBand (Default [ib_ipoib, nvme, nvme_fabrics, nvme_core])

Uninstall
---------
To uninstall, add '--tags ib_base_uninstall' to the ansible-playbook command or import uninstall.yml task directly from role.
    ansible-playbook -i inventory.yml playbook --tags ib_base_uninstall

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
