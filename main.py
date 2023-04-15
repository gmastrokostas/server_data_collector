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

#Variable data_items is a list that contains the variables for each table in our database.
#We call the file_processing class from the "process.py" file and we pass the
#variables from the "read_data".
#Read the comments on "app_variables.py" file under section "Process_data"

for file_type in app_variables.data_items:
    #calling class method dataprocessing from class file_processing
    read_data = file_processing(file_type, app_variables.servers_path, app_variables.servers_data_table, app_variables.rpm_data_table,
                                app_variables.storage_table, app_variables.network_setup_table, app_variables.network_interfaces_table,
                                app_variables.network_routes_table, app_variables.lvm_setup_table)
    read_data.dataprocessing()

uploader = data_upload(app_variables.servers_data_table, app_variables.rpm_data_table, app_variables.storage_table, app_variables.network_setup_table,
                       app_variables.network_interfaces_table, app_variables.network_routes_table, app_variables.lvm_setup_table, app_variables.servers_path)
uploader.upload()

