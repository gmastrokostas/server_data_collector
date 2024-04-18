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
# Copyright: (c) 2022, gmastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
import socket
import psutil

DOCUMENTATION = r'''
---
module: interface_info

short_description: Display network interfaces and IP assigned to them. This module has been tested on RedHat8/Centos8/Rock8 and it written under Python3.6


description: Display the names of all NetWork interfaces, their IPs and subnets.
             The module needs rpm python3-psutil installed on the remote nodes
             This module does not perform any changes.
             The info is contained in one main list and info for each interface 
             is a list it self with in the main list.
             List element position description
             [0] displays Interface name
             [1] displays IP
             [2] displays subnet
'''

EXAMPLES = r'''
- name: Display All Network Interface info
  interface_info:
  register: ifaceinfo
- debug:
    msg: "{{ifaceinfo}}"

- name: Search for specific interface name and IP
  interface_info:
  register: result
- debug:
    msg: "{{item}}"
  with_items:
  - "{{result.ifinfo}}"
  when:
   - (item[0] == 'team0' and item[1] == "192.168.2.200")
'''

def main():
    x = psutil.net_if_addrs().items()
    interface_info = []
    for intface, ipaddy in x:
        info = (intface, ipaddy[0][1], ipaddy[0][2])
        interface_info.append(info)
    module = AnsibleModule(argument_spec={})
    response = interface_info
    module.exit_json(changed=False, ifinfo=response)


if __name__ == '__main__':
    main()
