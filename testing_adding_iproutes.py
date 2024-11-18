from app_variables import save_yml_location
import os.path
import psycopg2
import ipaddress
#vars
#save_yml_location = "/home/seeker/stash/my_projects/server_data_collector/hostvars/"
hostname_file = 'inventory'
checK_file = os.path.isfile(hostname_file)
hostname_list = []
msg = """
Please make sure your inventory file is  called inventory
and that it exists in the same directory you are running
your script from.
"""
##Check if file with hostnames exists and if so,
#read it and insert the hostnames in a list
if  checK_file == False:
    print(msg)
elif checK_file == True:
    #This variables to be used int he query below
    interface_name = input("Enter interface name: ")
    #Following inputs to be used to generate the ip route command
    destination_ip = input("Enter destination IP: ")
    network_prefix = input("Enter network prefix: ")
    network_hosted = destination_ip + "/" + network_prefix
    try:
        ipaddress.ip_address(destination_ip) in ipaddress.ip_network(network_hosted)
    except ValueError:
        print("This is not a valid IP/Network. I am exiting")
        exit()
    #Opening file to read hostnames and insert them in a list
    f_open = open(hostname_file, encoding="utf-8")
    hostname_list_raw = f_open.readlines()
    #remove new line from list elements
    for x in hostname_list_raw:
        hostname_list.append(x.strip())
hostname_tuple = tuple(hostname_list)
interface_tuple = (interface_name,)
print(hostname_tuple)
input("Hello 1")
print(interface_tuple)
input("Hello press enter to continure")
#print(hostname_tuple)
#print(interface_tuple)

#query the database using the hostname_list
#Data stored in rows
conn = psycopg2.connect("dbname='serverdata' user='seeker'")
cur = conn.cursor()
#This is a view and not a table. It draws info from network_routes and network_interfaces tables.
#It will lookup only anything that is in hostname and ifname tuples
sql = """select hostname, gateway, ifname 
from view_interface_gateways 
where gateway !='0.0.0.0' and hostname in %s and ifname in %s
order by hostname;"""

cur.execute(sql, (hostname_tuple,interface_tuple,))
#The rows variable contains all the results from our query.
#We will use this in our for statements below
#to generate our commands.
rows = cur.fetchall()
for x in rows:
    print(x)

#These are the lists we will use
#To generate our IP route add commands.
dynamic_routes_list = [];
static_routes_list  = []
#These are the string we use to generate our commands
#in combination with the data we will get back from our sql query.
cli_string_1 = "ip route add";
cli_string_2 = "/";
cli_string_3 = "via ";
cli_string_4 = "dev "

perm_insrt_conf = []
#This for loop will generate our static and dynamic commands.
for net_data in rows:
    tuple_dynamic_route = cli_string_1+destination_ip+cli_string_2+network_prefix+cli_string_3+net_data[1]+cli_string_4, net_data[2]
    tuple_static_route = destination_ip+cli_string_2+network_prefix+cli_string_3+net_data[1]+cli_string_4, net_data[2]
    string_dynamic_route = str(tuple_dynamic_route)
    string_static_route  = str(tuple_static_route)
    host_name = net_data[0]

    # Generate and write the dynamic command
    full_save_path_dynamic = os.path.join(save_yml_location, host_name+"_dynamic_routes.yml")
    f1 = open(full_save_path_dynamic, "a")
    f1.write(cli_string_1 +  '\t' +   destination_ip +   cli_string_2 + network_prefix +  '\t' +  cli_string_3 + '\t' +  net_data[1] + '\t' +  cli_string_4 + '\t' + net_data[2] + '\n')
    f1.close()

    # Generate and write the static route command
    full_save_path_static = os.path.join(save_yml_location, host_name+".yml")
    f2 = open(full_save_path_static, "a")
    #f2.write(destination_ip+ '\t' + cli_string_2+ '\t' + network_prefix +  cli_string_3 + '\t' + net_data[1] + '\t' + cli_string_4 + '\t' +  net_data[2] + '\n')
    f2.write(destination_ip+cli_string_2 + network_prefix + '\t' +  cli_string_3 + '\t' + net_data[1] + '\t' + cli_string_4 + '\t' + net_data[2] + '\n')
    f2.close()
