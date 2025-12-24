# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *
import pyudev
import os
from pathlib import Path
import re
import os.path


def main():

    hardware_info_list = []
    context = pyudev.Context()

    for network_devices in context.list_devices(subsystem='net'):
        parent = network_devices.find_parent('pci')
        interface_name = (network_devices.sys_name)
        if parent:
            model = parent.get('ID_MODEL_FROM_DATABASE')
            info = (interface_name, model)
            hardware_info_list.append(info)

##############################################
##############################################

    #Detect if OS is virtual
    with open('/proc/cpuinfo','r') as f:
        vm_status ="hypervisor" in f.read()

    if_path = "/sys/class/net/"
    # x = os.path.islink(if_path)
    # print(x)
    # True
    # z = Path(if_path).resolve()
    # print(z)
    # /sys/devices/pci0000:00/0000:00:16.0/0000:0b:00.0/net/ens192
    # y = Path(if_path).as_posix()
    # print(y)
    # /sys/class/net/ens192

    regex_virtual = "virtual"
    numa_file_path = "/device/numa_node"
    #uevent_file_path = "/device/uevent"
    # These two variables show the PCIe gen type (1,2,3,4,5)
    # max_link shows what gen this device is.
    # current_link shows in what speed it is currently under. We may have a Gen5 device forced to be working as Gen3 device.
    # 2.5 GT/s → PCIe Gen1
    # 5.0 GT/s → PCIe Gen2
    # 8.0 GT/s → PCIe Gen3
    # 16.0 GT/s → PCIe Gen4
    # 32.0 GT/s → PCIe Gen5
    # 64.0 GT/s → PCIe Gen6
    max_link_width = "/device/max_link_width"
    current_link_width = "/device/current_link_width"
    max_link_speed = "/device/max_link_speed"
    current_link_speed = '/device/current_link_speed'
    ####
    #NIC Driver
    nic_driver='/device/driver'
    operstate_file = "/operstate"
    nic_index_file = "/ifindex"
    nic_speed_file = "/speed"
    nic_mtu_file = "/mtu"

    pci_if_devices = []
    #numa_info_list = []
    for entries in os.listdir(if_path):
        link_path = os.path.join(if_path, entries)
        if os.path.islink(link_path) is True:
            absolute_path = (Path(link_path).resolve())
            path_convert_to_string = (str(absolute_path))
            search_string = re.findall(regex_virtual, path_convert_to_string)
        # print(path_convert_to_string)
            if regex_virtual not in search_string:

                # DETECT LINK WIDTH
                if vm_status==True:
                    link_width_value="N/A"
                    link_current_value="N/A"
                    link_speed_value="N/A"
                    current_link_speed_value="N/A"
                    f_numa_value = "N/A"
                else:
                    m_link_width = path_convert_to_string + max_link_width
                    c_current_link_width = path_convert_to_string + current_link_width

                    f_open_link_width = open(m_link_width, "r")
                    f_open_current_width = open(c_current_link_width, "r")

                    link_width_value = f_open_link_width.read()
                    link_current_value = f_open_current_width.read()

                    # DETECT LINK SPEED
                    m_max_link_speed = path_convert_to_string + max_link_speed
                    c_current_link_speed = path_convert_to_string + current_link_speed

                    f_open_max_link_speed = open(m_max_link_speed, "r")
                    f_open_current_max_link_speed = open(c_current_link_speed, "r")

                    link_speed_value = f_open_max_link_speed.read()
                    current_link_speed_value = f_open_current_max_link_speed.read()
                ##################################################################################

                    # NUMA INFO
                    numa_ifs = path_convert_to_string + numa_file_path
                    f_open = open(numa_ifs, "r")
                    f_numa_value = f_open.read()

                # OPERSTATE INFO
                link_ifs = path_convert_to_string + operstate_file
                f_open_oper = open(link_ifs, "r")
                f_opersate_value = f_open_oper.read()
                # INDEX INFO
                index_ifs = path_convert_to_string + nic_index_file
                f_open_index = open(index_ifs, "r")
                f_ifindex_value = f_open_index.read()

                # MTU INFO
                index_ifs = path_convert_to_string + nic_mtu_file
                f_open_mtu = open(index_ifs, "r")
                f_mtu_value = f_open_mtu.read()

                # SPEED INFO
                speed_ifs = path_convert_to_string + nic_speed_file
                wireless_check = path_convert_to_string + "/wireless"
                ##############################################################################

                #NIC Driver info
                nic_driver_info=path_convert_to_string+nic_driver
                real_path_nic_driver=os.path.realpath(nic_driver_info)
                driver_path=real_path_nic_driver.split("/")
                driver=driver_path[5]

                #We will ignore wireless interfaces.
                if os.path.isdir(wireless_check):
                    f_speed_value = "N/A"
                else:
                    f_open_speed = open(speed_ifs, "r")
                    f_speed_value = f_open_speed.read()


                nic_cards = (entries, #NIC Name
                             f_numa_value, #NUMA Location
                             f_opersate_value, #If its up or down
                             f_ifindex_value, #index value of NIC
                             f_speed_value, #Speed in GBits
                             f_mtu_value, #MTU value
                             link_width_value, # the most PCIe lanes the device could use
                             link_current_value, # how many PCIe lanes it’s actually using right now
                             link_speed_value, # highest PCIe generation the hardware supports
                             current_link_speed_value, # speed at which the device is actually negotiated and running right now.
                             driver
                             )
                nic_cards_cleaned = tuple(item.strip() for item in nic_cards)

                pci_if_devices.append(nic_cards_cleaned)

    nic_state_info = {}

    for interfaces in pci_if_devices:
        x = nic_state_info[interfaces[0]] = list(interfaces[0:])

    for hardware in hardware_info_list:
        if hardware[0] in nic_state_info:
            nic_state_info[hardware[0]].extend(hardware[1:])

    module = AnsibleModule(argument_spec={})
    response = nic_state_info
    module.exit_json(changed=False, hardware_info=response)



if __name__ == '__main__':
    main()

