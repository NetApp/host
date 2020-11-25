netapp_eseries.host.ib_base
=========
    Install and configure base packages for InfiniBand.

Variables (Values specified are the defaults)
---------
eseries_ib_base_ipoib_enabled:          # Whether InfiniBand IPoIB should be configured (Default: false).
eseries_ib_base_iser_enabled:           # Whether InfiniBand iSER should be configured (Default: false).
eseries_ib_base_srp_enabled:            # Whether InfiniBand SRP should be configured (Default: false).
eseries_ib_base_rdma:                   # Directory for RDMA configuration files (Default: /etc/rdma/).
eseries_ib_base_rdma_memory_conf:       # Absolute path to the rdma.conf file for configuring rdma security limitations (Default: /etc/security/limits.d/rdma.conf).
eseries_ib_base_modules_d:              # Systemd module configuration files directory (Default: file/etc/modules-load.d/).
eseries_ib_base_ubuntu_packages:        # Packages to install for hosts running Ubuntu (Default: [infiniband-diags, rdma-core]).
eseries_ib_base_suse_packages:          # Packages to install for hosts running SUSE (Default: [infiniband-diags, rdma-core]).
eseries_ib_base_rhel_packages:          # Packages to install for hosts running RedHat (Default: [infiniband-diags, rdma-core]).
eseries_ib_base_kernel_modules:         # InfiniBand base kernel modules (Default: [ib_core, ib_umad, ib_uverbs, rdma_cm, rdma_ucm, mlx5_core, mlx5_ib])
eseries_ib_base_ipoib_kernel_modules:   # InfiniBand base kernel modules for InfiniBand IPoIB (Default: [ib_ipoib]).
eseries_ib_base_srp_kernel_modules:     # InfiniBand base kernel modules for InfiniBand SRP (Default: [ib_srp]).
eseries_ib_base_iser_kernel_modules:    # InfiniBand base kernel modules for InfiniBand iSER (Default: [ib_ipoib, ib_iser]).

Notes
-----
If using connectX-3 or earlier, override eseries_ib_base_kernel_modules and eseries_ib_base_uninstall_kernel_modules defaults in your inventory to use mlx4. Be sure to include all required modules.


Uninstall
---------
To uninstall, add '--tags ib_base_uninstall' to the ansible-playbook command.
    ansible-playbook -i inventory.yml playbook --tags ib_base_uninstall

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
