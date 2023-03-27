#INSTRUCTIONS
#sudo yum install gcc python38-devel postgresql-devel
#sudo yum install python38-pip
#sudo python3.8 -m pip install psycopg2-binary

import os
from process_data import file_processing
from upload_data import data_upload
from ansible_runner import run
import ansible_runner

#Run the playbook to collect the data first.
#playbook_path = "/home/seeker/stash/ansible/server_data_collector/server_collector.yml"
playbook_path="/home/seeker/stash/my_projects/server_data_collector/server_collector.yml"
# Define the inventory file
#inventory_path = "/home/seeker/stash/ansible/server_data_collector/inventory"
inventory_path = "/home/seeker/stash/my_projects/server_data_collector/inventory"

# File we capture our ensible errors 
#output_dir = "/home/seeker/stash/ansible/server_data_collector/logs"
output_dir = "/home/seeker/stash/my_projects/server_data_collector/logs"
# Define any extra variables
extra_vars = {
        "ansible_become": True,
        "ansible_become_user": "seeker",
        "become_sudo": True
        }
#TRY
try:
    result = run(
        playbook=playbook_path,
        inventory=inventory_path,
        extravars=extra_vars,
        )
    #r = ansible_runner.Runner(
    #playbook=playbook_path,
    #extravars=extra_vars,
    #inventory=inventory_path,
    #json_mode=True,
    #quiet=True
    #)
    if result.status == "failed":
        for host_result in result.events:
            print(host_result['event_data']['stdout'])
            print(host_result['event_data']['stderr'])
except Exception as e:
    print(e)

# Print the result
print(result.rc)
print(result.status)
print(result.events)
print(result.run())
print(result.errored)


#IF everything worked with the playbook then upload the data to the database.

# This directory has the csv files ansible creates and fetches with
# data from the servers
servers_path = "/home/seeker/stash/ansible/server_data_collector/servers"
# the csv_file variable will be assigned one of these variables
# depending what info we pass when we call this class.
servers_data_table = "/home/seeker/stash/ansible/server_data_collector/datafiles/a1servers"
rpm_data_table = "/home/seeker/stash/ansible/server_data_collector/datafiles/rpm_packages"
storage_table  = "/home/seeker/stash/ansible/server_data_collector/datafiles/storage_capacity"
network_setup_table =  "/home/seeker/stash/ansible/server_data_collector/datafiles/network_setup"
network_interfaces_table = "/home/seeker/stash/ansible/server_data_collector/datafiles/network_interfaces"
network_routes_table = "/home/seeker/stash/ansible/server_data_collector/datafiles/network_routes"
lvm_setup_table="/home/seeker/stash/ansible/server_data_collector/datafiles/lvm_setup"

data_items = ["servers", "rpm", "storage", "network_setup", "network_interfaces", "network_routes", "lvm_setup"]
for file_type in data_items:
    #calling class method dataprocessing from class file_processing
    read_data = file_processing(file_type, servers_path, servers_data_table, rpm_data_table,
                                storage_table, network_setup_table, network_interfaces_table,
                                network_routes_table, lvm_setup_table)
    read_data.dataprocessing()

uploader = data_upload(servers_data_table, rpm_data_table, storage_table, network_setup_table,
                       network_interfaces_table, network_routes_table, lvm_setup_table, servers_path)
uploader.upload()

