common/interface/firewall_zone/ is a common set of tasks intended to add interface(s) to firewall zones.

eseries_common_interfaces:      # List of interfaces. Each interface dictionary may have an 'zone' key to specify a firewall zone unique to it.
eseries_common_firewall_zone:   # Default firewall zone.
eseries_common_firewall_configure # Set to false to skip attempting to configure the firewall even if firewalld or ufw are installed.