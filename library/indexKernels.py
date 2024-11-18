# -*- coding: utf-8 -*-
# Copyright: (c) 2022, george.mastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
import glob
import os
from os.path import exists


DOCUMENTATION = r'''
---
module: indexKernels 

short_description: Indexed display of installed kernels in desceding order. This module has been tested on RedHat8/Centos8/Rock8 and it written under Python3.6


description: Modules reads the entries from /boot/loader/entries/.
             It lists the entries in a descending order, from newest to oldest.
             It follows the indexing pattern  of sudo grubby --info=ALL
             This module does not perform any changes.
             The info is contained in one main list and info for all kernel entries 
             Positional List element position description
             Position: 
             [0] equates to kernel index 0
             [1] equates to kernel index 1
             [2] equates to kernel index 2
'''

EXAMPLES = r'''
- name: Display All kernels
  indexKernels:
  register: results
- debug:
    msg: "{{results}}"

- name: List kernel with index 1
  indexKernels:
  register: result
- debug:
    msg: "{{item}}"
  with_items:
  - "{{result.kernelindexes[1]}}"
'''

def main():
    root_path = glob.glob('/boot/loader/entries/*.conf')
    root_path.sort(key=os.path.getatime)
    bootloaderentries = "/boot/loader/entries/"
    check_file = exists(bootloaderentries)
    kernel_versions = []
    confstring = ".conf"

    if check_file is True:
        full_kernel_string = ("\n".join(root_path).split("\n"))
        for x in full_kernel_string:
            major = (x.split("-")[1])
            minor = (x.split("-")[2])
            kernel_string = major + minor.replace(confstring, "")
            kernel_versions.append(kernel_string)
            # kernels_indexed = enumerate(kernel_versions)

    elif check_file is False:
        kernel_versions = []
        #exit()


    module = AnsibleModule(argument_spec={})
    response = kernel_versions
    module.exit_json(changed=False, kernelindexes=response)


if __name__ == '__main__':
    main()
