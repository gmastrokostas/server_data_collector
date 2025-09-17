# Copyright (C) 2024  GEORGE MASTROKOSTAS
# This file is part of SERVER_DATA_COLLECTOR.
#
# SERVER_DATA_COLLECTOR is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# YOUR_PROJECT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
#Run the playbook to collect the data first.
get_cwd=os.getcwd()
playbook_path=get_cwd+"/server_collector.yml"
# Define the inventory file
inventory_path =get_cwd+"/inventory"
# File we capture our ensible errors
output_dir = get_cwd+"/logs"
# Define any extra variables

extra_vars = {
        "ansible_become": True,
        "ansible_become_user": "seeker",
        "become_sudo": True
        }
#Process_data
# This directory has the csv files ansible creates and fetches with
# data from each individual server.
#ex: servers/var/tmp/servers.csv
#99337333|nerdy|2025-08-03|08:16:04|RedHat|9.6|....
servers_path = get_cwd+"/servers"

#This is the location of all the data from all servers is collected.
#For example the "/datafiles/a1servers" contains the info from all
#all servers in the "servers/var/tmp/servers.csv" file (see above.
#Also very important, the files below are named after the actual
#database tables we will store the info.
servers_data_table = get_cwd+"/datafiles/a1servers"
rpm_data_table = get_cwd+"/datafiles/rpm_packages"
storage_table = get_cwd+"/datafiles/storage_capacity"
network_setup_table = get_cwd+"/datafiles/network_setup"
network_interfaces_table = get_cwd+"/datafiles/network_interfaces"
network_routes_table = get_cwd+"/datafiles/network_routes"
lvm_setup_table=get_cwd+"/datafiles/lvm_setup"
yml_file_location=get_cwd+"/hostvars"
save_yml_location=get_cwd+"/hostvars"

#This list will be used by main.py 
#Read the comments in the main.py for more information.
data_items = ["servers", "rpm", "storage", "network_setup", "network_interfaces", "network_routes", "lvm_setup"]
