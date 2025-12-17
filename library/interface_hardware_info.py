# -*- coding: utf-8 -*-
# Copyright: (c) 2022, gmastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
import pyudev


def main():
    
    hardware_info_list=[]
    
    context=pyudev.Context()

    for network_devices in context.list_devices(subsystem='net'):
        parent=network_devices.find_parent('pci')
        interface_name=(network_devices.sys_name)
        if parent:
            pci_id=parent.get('PCI_ID')
            vendor=parent.get('ID_VENDOR_FROM_DATABASE')
            model=parent.get('ID_MODEL_FROM_DATABASE')
            info=(interface_name, pci_id, vendor, model)
            hardware_info_list.append(info)
    module = AnsibleModule(argument_spec={})
    response = hardware_info_list
    module.exit_json(changed=False, ifinfo=response)
    
            
if __name__ == '__main__':
    main()

