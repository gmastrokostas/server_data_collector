#This file is part of server data collector.
#Copyright (C) 2022 - George Mastrokostas
#email: gmastrokostas@gmail.com

#server data collector is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#########################################################################


# -*- coding: utf-8 -*-
# Copyright: (c) 2022, george.mastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
import re
from pathlib import Path
import os


DOCUMENTATION = r'''
---
module: lvm_info

short_description: Display which NUMA node aNIC belongs to.


description: Display in which NUMA node a NIC belongs to..
             Info is captured from '/sys/class/net/"NIC_NAME"/device'
             This module does not perform any changes.
             The info is contained in one main list.
             List element position description
             [0] Interface name
             [1] NUMA valie

'''

EXAMPLES = r'''
- hosts: all
  tasks:
  - name: LOL
    nic_numa_info:
    register: info
  - debug:
      msg: "{{info.nicnumainfo}}"
'''
def main():
    if_path = "/sys/class/net/"
    x = os.path.islink(if_path)
    # print(x)
    # True
    z = Path(if_path).resolve()
    # print(z)
    # /sys/devices/pci0000:00/0000:00:16.0/0000:0b:00.0/net/ens192
    y = Path(if_path).as_posix()
    # print(y)
    # /sys/class/net/ens192

    regex_virtual = "virtual"
    numa_file_path = "/device/numa_node"

    pci_if_devices = []
    numa_info_list=[]
    for entries in os.listdir(if_path):
        link_path = os.path.join(if_path, entries)
        if os.path.islink(link_path) is True:
            absolute_path = (Path(link_path).resolve())
            path_convert_to_string = (str(absolute_path))
            search_string = re.findall(regex_virtual, path_convert_to_string)
            # print(path_convert_to_string)
            if regex_virtual not in search_string:
                pci_ifs = path_convert_to_string + numa_file_path
                if_name = path_convert_to_string.split("/")[7]
                f_open = open(pci_ifs, "r")
                f_numa_value = f_open.read()
                # We need to get rid of the \n line on each element of the list
                for elements in range(len(f_numa_value)):
                    f_numa_value_clean = f_numa_value.replace('\n', '')
                pci_cards = if_name, f_numa_value_clean
                for data in pci_cards:
                    numa_info_list.append(data)

    module = AnsibleModule(argument_spec={})
    response =numa_info_list
    module.exit_json(changed=False, nicnumainfo=response)


if __name__ == '__main__':
    main()
