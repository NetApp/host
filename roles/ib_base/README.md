netapp_eseries.host.ib_base
=========
    Install and configure base packages for InfiniBand.

Variables (Values specified are the defaults)
---------
eseries_ib_base_ipoib_enabled: false                                # Whether RDMA should be configured for InfiniBand IPoIB.
eseries_ib_base_iser_enabled: false                                 # Whether RDMA should be configured for InfiniBand iSER.
eseries_ib_base_srp_enabled: false                                  # Whether RDMA should be configured for InfiniBand SRP.
eseries_ib_base_rdma_conf: /etc/rdma/rdma.conf                      # Absolute path to the rdma.conf file for configuring rdma modules.
eseries_ib_base_rdma_memory_conf: /etc/security/limits.d/rdma.conf  # Absolute path to the rdma.conf file for configuring rdma security limitations.
eseries_ib_base_ubuntu_packages:                                    # Packages to install for hosts running Ubuntu
  - rdma-core
  - infiniband-diags
eseries_ib_base_suse_packages:                                      # Packages to install for hosts running SUSE
  - rdma-core
  - infiniband-diags
eseries_ib_base_rhel_packages:                                      # Packages to install for hosts running RHEL
  - rdma-core
  - infiniband-diags
eseries_ib_base_kernel_modules:                                     # InfiniBand base kernel modules.
  - rdma_cm
  - mlx5_core
eseries_ib_ipoib_kernel_modules:                                    # InfiniBand IPoIB kernel modules.
  - ib_ipoib
eseries_ib_srp_kernel_modules:                                      # InfiniBand SRP kernel modules.
  - ib_srp
eseries_ib_iser_kernel_modules:                                     # InfiniBand iSER kernel modules.
  - ib_iser
eseries_ib_base_uninstall_kernel_modules:                           # InfiniBand kernel modules that should be unloaded during uninstallation.
  - mlx5_ib
  - mlx5_core
  - ib_ipoib
  - ib_iser
  - ib_srp

Notes
-----
If using connectX-3 or earlier, override eseries_ib_base_kernel_modules and eseries_ib_base_uninstall_kernel_modules defaults in your inventory to use mlx4.


Uninstall
---------
To uninstall InfiniBand IPoIB, add '--tags ib_base_uninstall' to the ansible-playbook command. Note that only kernel modules mlx5_ib, mlx5_core, ib_ipoib, ib_iser and ib_srp will be unloaded.

    ansible-playbook -i inventory.yml playbook --tags ib_base_uninstall

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)
