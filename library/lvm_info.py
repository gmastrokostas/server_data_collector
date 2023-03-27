# -*- coding: utf-8 -*-
# Copyright: (c) 2022, george mastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/usr/bin/python
from ansible.module_utils.basic import *
import os
import stat

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
    lvm_list = []
    # id_directory = '/dev/disk/by-id/'
    # Dive into mapper to see in what DM-* LVM is being pointed to.
    id_directory = '/dev/mapper/'
    for root, dirs, files in os.walk(id_directory):
        for f in files:
            # Full path of /dev/mapper/*
            full_path_to_file = root + f
            # However the above leads to the the actual real path
            # example of what I am saying above and what the actual real path is. /dev/mapper/rl_hpv1-root -> ../dm-0
            real_path = os.path.realpath(full_path_to_file)

            # Make sure the above are block files.
            if stat.S_ISBLK(os.stat(real_path).st_mode) is True:
                # print(real_path, " ", full_path_to_file)
                # Here start parsing the DM to dive into the /sys dir
                # You are now parsing /dev/dm-*
                # Here start parsing the DM to dive into the /sys dir
                dm_parse = real_path.split("/")
                # You are now grabbing item No2 from the split above and you
                # are combing it with the /sys/block and /slaves directories.
                # This will produce the path of /sys/block/dm-*/slaves
                # The "slaves" directory contains the drives of the drives
                # that belong to each specific DM-* (aka LVM)
                dm_slaves_sys_path = "/sys/block/" + dm_parse[2] + "/slaves"
                vg_name_entry = full_path_to_file.split("/")[3]
                # You will now use /dev/mapper/"name_of_lvm"
                # And you will parse the last entries under
                # /dev/mapper/. So for example /dev/mapper/ has cs-root and cs-swap
                # Linux always does this. The first entry cs is the VG and second entry after - is the LV
                vg_name = vg_name_entry.split("-")[0]
                lv_name = vg_name_entry.split("-")[1]
                # Now you will dive in the /sys/block/dm-*/slaves and see whuch drives belong on each DM-*
                dir_list = os.listdir(dm_slaves_sys_path)
                for i in dir_list:
                    # Here you conbine the drives with the vg_name and lv_name
                    info = i, vg_name, lv_name,full_path_to_file
                    lvm_list.append(info)
    module = AnsibleModule(argument_spec={})
    response = lvm_list
    module.exit_json(changed=False, lvminfo=response)


if __name__ == '__main__':
    main()













































