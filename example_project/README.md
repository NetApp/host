Example Project for E-Series Ansible Automation
===============================================

The purpose of this example project is to provide a starting framework for an end-to-end deployment of E-Series storage systems. Provided your E-Series storage has been physically installed with DHCP-assigned addresses, this automation will be able to discover the storage systems based on the system's serial number which is located on the top-front-left label of the device. Once discovered, the storage system will be assigned the provided admin password, configure static IPv4 management addresses, configure hostside interfaces, provision and map storage to hosts. Next, the automation will install multipath, configure requirements for the needed communication protocol, and create persistent mounts on the hosts with mapped volumes. For this automation to be successful, it is necessary to define the inventory for not only the storage systems but also the hosts with mapped volumes.


Project Requirements
--------------------
Ansible control node with Ansible version 2.10 or later installed
    $ pip install ansible netaddr ipaddr

NetApp E-Series automation ecosystem
    $ ansible-galaxy collection install netapp_eseries.santricity
    $ ansible-galaxy collection install netapp_eseries.host


Using the Example Project
-------------------------
1) Copy and update example_project directory to the desired location.

2) Update ./inventory.yml to reflect your storage systems and hosts.

3) Update ./group_vars/eseries_storage_systems.yml if utilizing SANtricity Web Services Proxy.

4) Create inventory host files for each storage system.
    Copy and update eseries_*_example_array.yml file with the name of the storage system, and then update its contents to the system's desired state.

5) Create inventory host files for each storage system host.
    Copy and update eseries_*_example_host.yml file with the name of the host, and then update its contents to the host's desired state.


Project Ansible Commands
------------------------
Configure SANtricity Web Services Proxy command (Optional)
    $ ansible-playbook -i inventory.yml web_services_proxy_playbook.yml

Configure E-Series storage systems command
    $ ansible-playbook -i inventory.yml playbook.yml


License
-------
    BSD-3-Clause


Author Information
------------------
    Nathan Swartz (@ndswartz)
