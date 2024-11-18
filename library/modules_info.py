# -*- coding: utf-8 -*-
# Copyright: (c) 2022, george mastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
from os.path import exists

DOCUMENTATION = r'''
---
module: modules_info

short_description: Display all running modules. This module has been tested on RedHat8/Centos8/Rock8 and it written under Python3.6


description: Display all running modules. 
             Info is captured from '/proc/modules'
             It displays, name, size, number of other modules using this module, name of modules using this module
             This module does not perform any changes.
             The info is contained in one main list and info for each module is 
             a list it self with in the main list.
             List element position description
             [0] displays Module name
             [1] displays Memory size
             [2] displays Number of modules using this module
             [3] displays names of modules using this module
'''

EXAMPLES = r'''
- name: Display All Running modules
  interface_info:
  register: moduleinfo
- debug:
    msg: "{{moduleinfo}}"

- name: Search for specific running module
  interface_info:
  register: result
- debug:
    msg: "{{item}}"
  with_items:
  - "{{result.moduleinfo}}"
  when:
   - (item[0] == 'realtek')
'''
def main():
    modules_info = '/proc/modules1'
    check_file = exists(modules_info)
    modules_list = []
    if check_file is True:
        with open(modules_info) as f:
            lines = f.readlines()
            for x in lines:
                module_name = (x.split()[0])
                module_size = (x.split()[1])
                module_proc = (x.split()[2])
                module_deps = (x.split()[3])
                info = (module_name, module_size, module_proc, module_deps)
                modules_list.append(info)
    elif check_file is False:
        #modules_list = "Operating System is not supported"
        modules_list = []


    module = AnsibleModule(argument_spec={})
    response = modules_list
    module.exit_json(changed=False, moduleinfo=response)

if __name__ == '__main__':
    main()

