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

short_description: Display associations between drives and PVs and VGs and LVs.


description: Display associations between drives and LVM (PV/VG/LV).
             Info is captured from '/dev/mapper/'
             This module does not perform any changes.
             The info is contained in one main list.
             List element position description
             [0] displays drive 
             [1] displays Volume Groups associated with each drive
             [2] displays Logical Groups associated with each Volume Groups

'''

EXAMPLES = r'''
- name: Display All LVM Info
  lvm_info:
  register: kvminfo
- debug:
    msg: "{{lvminfo}}"
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
                f_open = open(pci_ifs, "r")
                f_numa_value = f_open.read()
                # print(f_numa_value)
                pci_cards = path_convert_to_string, f_numa_value
                # pci_if_devices.append(pci_ifs+numa_file_path)
                for data in pci_cards:
                    numa_info_list.append(data)
    module = AnsibleModule(argument_spec={})
    response =numa_info_list
    module.exit_json(changed=False, numainfo=response)

