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
# data from the servers
servers_path = get_cwd+"/servers"
# the csv_file variable will be assigned one of these variables
# depending what info we pass when we call this class.
servers_data_table = get_cwd+"/datafiles/a1servers"
rpm_data_table = get_cwd+"/datafiles/rpm_packages"
storage_table = get_cwd+"/datafiles/storage_capacity"
network_setup_table = get_cwd+"/datafiles/network_setup"
network_interfaces_table = get_cwd+"/datafiles/network_interfaces"
network_routes_table = get_cwd+"/datafiles/network_routes"
lvm_setup_table=get_cwd+"/datafiles/lvm_setup"
yml_file_location=get_cwd+"/hostvars"
save_yml_location=get_cwd+"/hostvars"
data_items = ["servers", "rpm", "storage", "network_setup", "network_interfaces", "network_routes", "lvm_setup"]
