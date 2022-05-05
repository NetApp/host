# netapp_eseries.host.nvme_roce
    Ensure NVMe RoCE is configured on host.

## Role Variables
    eseries_roce_configure_network:         # Whether to configure iSCSI network interfaces. Choices: true, false (Default: true)
    eseries_roce_configure_firewall:        # Whether to configure firewall. Choices true, false (Default: true)
    eseries_roce_interfaces:                # (Required) List of IP-based interfaces.
      - name:                                    # (Required) Name of interface (i.e. ib0, eth0, em1, ens160).
        address:                                 # (Required) IPv4 address. Use the format 192.0.2.24/24.
        hook_templates:                          # List of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                                 #   the interface variable within the hook templates).
        zone:                                    # Firewall zone. If the zone does not exist then it will be created. (Note: Only implemented for firewalld)
        (...)                                    # Add any valid key-value pair for the expected Netplan or ifcfg-x configuration files. Be sure to quote recognized
                                                 #   boolean values (on, off, yes, no, etc.) otherwise they will be converted into True/False.
        iface:                                   # Dictionary defining additional interface information for open-iscsi (<iscsi_dir>/iface/<interface>).
        node:                                    # Dictionary defining additional targets information for open-iscsi (<iscsi_dir>/nodes/<target_iqn>/<address>,<port>,[0-9]+/<interface>).
                                                 #   Look at /etc/iscsi/iscsid.conf for options.
    eseries_roce_default_hook_templates:    # Default list of hook templates for Network Manager dispatcher (interface definition will be accessible through
                                                 #    the interface variable within the hook templates).
    eseries_roce_firewall_zone:             # Default firewall zone. (Note: Only implemented for firewalld)
    eseries_roce_nqn:                       # Host NVMe qualified name.

## Notes
    WARNING! Role will configure the specified network interfaces unless eseries_roce_configure_network is set to false.

## License
    BSD-3-Clause

## Author Information
    Nathan Swartz (@ndswartz)


Role Variables
--------------
eseries_nvme_nqn:                                   # Host NQN. When not specified, nqn will be derived from host.
eseries_nvme_ib_interfaces:                         # (Required) List of NVMe InfiniBand interfaces.
  - name:                                           # (Required) Name of NVMe InfiniBand  interface (i.e. ib0, ib1).
    address:                                        # (Required) IPv4 address. Use CIDR form (ex. 192.168.1.1/24).
    port:                                           # Interface NVMe IPoIB listening port.
    mtu:                                            # Interface maximum transmission unit measured in bytes.
    queue_depth:                                    # Session queue depth.
    configure:                                      # Whether to configure OpenSM for interface.
    subnet_prefix:                                  # OpenSM subnet manager's subnet prefix.
    priority:                                       # OpenSM subnet manager's priority.

eseries_nvme_ib_username:                           # Default Storage target CHAP username (Default: "").
eseries_nvme_ib_password:                           # Default Storage target CHAP password (Default: "").
eseries_nvme_ib_mtu:                                # Default maximum transmission unit measured in bytes (Default: "").
eseries_nvme_ib_queue_depth:                        # Default queue depth (Default: 32).
eseries_nvme_ib_session_replacement_timeout:        # Default session replacement should a timeout occur (Default: 20).
eseries_nvme_ib_service_name:                       # Custom NVMe over InfiniBand systemd service name (Default: eseries_nvme_ib.service).

General Notes
-------------
A customized systemd service daemon will be generated based on the required targets needed for existing storage system mappings. You can view the generated daemon at /etc/nvme/eseries_nvme_ib_daemon. The daemon is controlled with the systemd service eseries_nvme_ib.service which will ensure connectivity during boot.

License
-------
    BSD-3-Clause

Author Information
------------------
    Nathan Swartz (@ndswartz)