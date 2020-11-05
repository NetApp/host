netapp_eseries.host.srp
=========
    Configures InfiniBand SRP which installs and configure packages, kernel modules, and configures InfiniBand subnet manager if needed.

Role Variables
--------------
eseries_ib_opensm_subnet_manager_configure:    # Default for whether to configure OpenSM (Default: false).
eseries_ib_opensm_subnet_prefix_base:          # Default OpenSM subnet manager's subnet prefix base. The last two digits will be determined by device port ordering (Default: "0xfe800000000000").
eseries_ib_opensm_subnet_priority:             # Default OpenSM subnet manager's priority. eseries_ib_iser_opensm_subnet_priority can be used instead (Default: 0). Choices: 0-15 (15 is highest priority).
eseries_ib_opensm_interfaces:                  # List of InfiniBand interfaces.
  - name:                                      # (Required) Use the name of InfiniBand interface (i.e. ib0, ib1) when IPoIB has been configured, otherwise use <DEVICE>_<PORT> (i.e. mlx5_0_1, mlx5_0_2)
    configure:                                 # Whether to configure OpenSM for port (Default: True).
    subnet_prefix:                             # OpenSM subnet manager's subnet prefix.
    priority:                                  # OpenSM subnet manager's priority.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)