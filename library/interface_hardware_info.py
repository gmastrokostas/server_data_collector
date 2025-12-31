# -*- coding: utf-8 -*-
# Copyright: (c) 2022, gmastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
import pyudev

DOCUMENTATION = r'''
---
module: interface_hardware_info.p

short_description: Display hardware information for your network interfaces. This module has been tested with RHLE8/9. It requires the python3-pyudev rpm package.


description: Display interface names, vendor device number, vendor, model.
             The module needs rpm python3-pyudev installed on the remote nodes
             This module does not perform any changes.
             The information is contained in one main list and information for each interface
             is a list it self and information for each interface is its own tuple.
             List element position description
             [0] interface name
             [1] vendor device number
             [2] vendor name
             [3] model
'''

EXAMPLES = r'''
- name: Display All Network Interface info
  hardware_info_list:
  register: ifacehardinfo
- debug:
    msg: "{{ifacehardinfo}}"

- name: Search for specific interface name and model
  hardware_info_list::
  register: result
- debug:
    msg: "{{item}}"
  with_items:
  - "{{result.ifinfo}}"
  when:
   - (item[0] == 'eth0' and item[1] == "Melanox")
'''

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

