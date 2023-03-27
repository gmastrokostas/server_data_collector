# -*- coding: utf-8 -*-
# Copyright: (c) 2022, george.mastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
from os.path import exists
import struct
import socket
import ipaddress

DOCUMENTATION = r'''
---
module: routing_table_info

short_description: Display routing table. This module has been tested on RedHat8/Centos8/Rock8 and it written under Python3.6


description: Display the routing table of a Linux server.
             The info is captured by reading /proc/net/route
             This module does not perform any changes.
             The info is contained in one main list and each route is its own list.
             List element position description
             [0] displays Interface name
             [1] displays Destination
             [2] displays Gateway
             [7] displays NetMask
'''

EXAMPLES = r'''
- name: Display all routes
  routing_table_info:
  register: routesinfo
- debug:
    msg: "{{routesinfo}}"

- name: Display Routing info for a specific interface
- debug:
    msg: "{{item}}"
  with_items:
    - "{{routesinfo.routes}}"
  when:
    - (item[0] == 'team0')
'''

def main():
    routes_path = '/proc/net/route'
    check_file = exists(routes_path)
    routing_table_facts = []
    if check_file is True:
        # Open the file in read mode
        with open(routes_path) as f:
            lines = f.readlines()
            for x in lines[1:]:  # Skip the headers/title
                # Parse it. You want fields 0-Device 1-Destination 2-Gateway 7-NetMask
                # print(x.strip().split())
                iface = (x.strip().split()[0])

                dest = (x.strip().split()[1])
                dest_int = int(dest, 16)
                dest_ip_address = socket.inet_ntoa(struct.pack("<L", dest_int))

                gtw = (x.strip().split()[2])
                gtw_int = int(gtw, 16)
                gtw_ip_address = socket.inet_ntoa(struct.pack("<L", gtw_int))

                netm = (x.strip().split()[7])
                netm_int = int(netm, 16)
                netm_ip_address = socket.inet_ntoa(struct.pack("<L", netm_int))
                info = (iface, dest_ip_address, gtw_ip_address, netm_ip_address)
                routing_table_facts.append(info)
    elif check_file is False:
        routing_table_facts = []

    module = AnsibleModule(argument_spec={})
    response = routing_table_facts
    module.exit_json(changed=False, routes=response)

if __name__ == '__main__':
    main()

