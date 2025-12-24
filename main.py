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

#INSTRUCTIONS
#sudo yum install gcc python38-devel postgresql-devel
#sudo yum install python38-pip
#sudo python3.8 -m pip install psycopg2-binary

import os
from process_data import file_processing
from upload_data import data_upload
from ansible_runner import run
#This python file contains all of our variables
import app_variables
import ansible_runner

#We will run our ansible role(s) via python.
# Define extra ansible variables

#TRY
#Run our playbook that calls the role.
try:
    result = run(
        playbook=app_variables.playbook_path,
        inventory=app_variables.inventory_path,
        extravars=app_variables.extra_vars,
        )

    if result.status == "failed":
        for host_result in result.events:
            print(host_result['event_data']['stdout'])
            print(host_result['event_data']['stderr'])
except Exception as e:
    print(e)

# Print the result

#IF everything worked with the playbook then upload the data to the database.

#Variable data_items will be used by process_data.py to determine which type of information
#We will process. See the "if" statements in the process_data.py.
#if file_type==servers then we will proccess the info in the a1servers file
#and the destination file will be servers.csv.
#At that point the type of file will determine the file path.
#in this example the path will be the variable servers_data_table which all the data for 
#servers for each device will be appended on.
#
#We call the file_processing class from the "process.py" file and we pass the
#variables from the "read_data".
#Read the comments on "app_variables.py" file under section "Process_data"

for file_type in app_variables.data_items:
    #calling class method dataprocessing from class file_processing
    read_data = file_processing(
                                file_type,
                                app_variables.servers_path,
                                app_variables.servers_data_table,
                                app_variables.rpm_data_table,
                                app_variables.storage_table,
                                app_variables.network_setup_table,
                                app_variables.network_interfaces_table,
                                app_variables.network_routes_table,
                                app_variables.lvm_setup_table,
                                app_variables.interface_hardware_info_table,
                                app_variables.nic_hardw_state_table)
    read_data.dataprocessing()

uploader = data_upload(app_variables.servers_data_table,
                       app_variables.rpm_data_table,
                       app_variables.storage_table,
                       app_variables.network_setup_table,
                       app_variables.network_interfaces_table,
                       app_variables.network_routes_table,
                       app_variables.lvm_setup_table,
                       app_variables.interface_hardware_info_table,
                       app_variables.nic_hardw_state_table,
                       app_variables.servers_path)
uploader.upload()

