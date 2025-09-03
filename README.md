# server_data_collector  v 0.6

# FOR INSTALLATION AND INSTRUCTIONS READ the "instructions" file


----------------------
Document Sections:

1-  Purpose

2-  Tools used to capture data:

3-  Server Requirements:

4-  Logical Diagram of how Data is captured and stored

5-  Database Setup

6-  Database Tables

7-  Data Captured

8-  To Do




1- Purpose:
----------- 

Collect and access at scale server setup/environment data.
Makes network, software, storage, hardware audits of the servers easy and fast.

Data is collected with Ansible, processed with Python and uploaded to a PostgreSQL database.

In addition, custom queries and custom python scripts or ansible playbooks can be written to perform
sanity checks, generate template files for changes for large number of servers.


2- Summary of how it works:
-----------------------
It is agentless. From a single control node, data is captured via ansible (ansible facts) and jinja2 templates.
The jinja2 files are created on the server and then brought back to the ansible control node.
At that point the data is uploaded on the database which runs on the same ansible controls node.
None of the remote servers interact with the database. As a result there is no need to setup sql clients on the servers.
The database is completely isolated from the network and is configured to deny any network connections.
All connections are made only via ansible through SSH.


3- Logical Diagram of how Data is captured and stored:
---------------------------------------------------

                   Single Control node
          +-----------------------------------+
          |     Data is uploaded in Database  |
          |     ---------------------------   |
          |                 ∧                 |
          |     Data is stored in CVS files   |
          |     ---------------------------   |
          |                 ∧                 |
          |     Ansible captures server data  |
          |     ----------------------------  |
          -------------------------------------
                           ∧
     Jinja2 templates are deployd and fetched back as CSV files
                           v
     -------------  -------------   -------------  -------------
     |  server   |  |  server   |   |   server  |  |   server  |
     ------------   -------------   -------------  -------------



4- Case Examples (all these are done at scale):
---------------------------------------
- Network route traffic sanity check: Check if server traffic is going out through the correct interface 
  by comparing the server route entries against a series of routes in a database table.

- At scale automation config file generation to be deployed.
  Generate ansible host_vars files to add dynamic and static routes on servers. Each generated yml file 
  is associated with the given server and the given server’s individual routing information. 
  If the new routing information entered by the end user do not correspond to an actual interface name 
  and/or if the IP is not an actual IP, the files are not generated.

- To expand on the above example, you can query the database to find which servers talk to a specific network.
  For example you may want to find out which servers talk to a specific venue, or have to the outside world.

- Instant Search for specific RPM packages and their versions across the whole estate.
  This allows for the instant search of RPM packages across the whole estate.




5- Requirements
--------------------------
SOFTWARE For the Control Node:
 - Redhat/CentOS/Rocky - 8/9
 - Ansible v 2.9
 - Postgres 14/15
 - Python3.6

HARDWARE for the Control Node:
1 VM with 1 GIG of RAM and 60GIGs of space.
Plans are underway to make this a container.


SOFTWARE on the Remote Servers:
 - python36-pusitls (RPM is part of the official Repos)
 - ssh


6- Data Capture with Ansible
-----------------------------
The ansible role/playbook which captures this data requires sudo access on the remote servers.
For consistency and to avoid issues with permissions when uploading data in the database, 
the Linux account used with the ansible role has the same name as the database role used to
manage this data in the database.

The data is captured with the use of ansible by deploying jinja2 templates which reference 
ansible facts from each server. These facts are captured through the default ansible
facts and also from  the use of custom written ansible modules written in python3.6.
The latter was done to address limitations with how the default ansible facts are organized.

As per the "template" ansible module, the jinja2 templates are deployed on the 
remote servers where the facts/variables are being populated with the appropriate values per each server.
The location of these files is in “/var/tmp” but this can be easily changed to a different location.

Once the templates are populated with data then the files are brought back through the use of the “fetch” 
ansible module and stored as “CSV” files in the control node. The upload of data in the database is done
through the use of custom Python scripts since the postgresSQL ansible module does not appear to be
maintained with vigor by the ansible community and it often breaks.

The type of data these templates capture is described in the “database tables” section of this document.


7- List and Description of the custom Ansible modules
--------------------------------------------------
The modules are not placed in the default ansible module location. 
This is done to keep the default install of ansible as is. 
Instead they are placed in the directory called “library” in the same location where the playbook/role is run from.
All the custom ansible modules were created with Python3.6. 
Only the default python modules were used. All of the custom modules are unable to perform any system changes.
They just capture data from the remote servers.


8- List of custom ansible modules created:
---------------------------------------
- network_routes.py: Data is captured from “/proc/net/route”

- modules_info.py: Data is captured from “/proc/modules”

- lvm_info.py: Data is captured from “/dev/mapper” and “/sys/block”

- interface_info.py: Data is captured by using the socket and psutil python default modules

- hypervisor_info.py: Data is captured by using the “libvirt” python module. This module is installed by default if a server is a KVM server.


9- Processing and Uploading to the database the data:
-----------------------------------------------------
After ansible is done fetching the files with the server data, then a series of python scripts
upload the data into the database. These scripts do not need sudo access and they all reside/owned
under the Linux “seeker” account, the same account used with ansible.

However, the default admin database account “postgres” needs to have access to the associated directories
from where the data are uploaded from. The “postgres” account is not used in any way to upload/manipulate
any of the data, but the account needs to be aware of these directories from where the data is coming from.

Access to these directories to the “postgres” account is granted through the use strict Linux ACL permissions,
which explicitly allow access only to the default “postgres” account.
Reminder: the “postgres” account has no login permissions. 

The processing of data and upload of data is done through the “main.py", “process_data.py” and “upload_data.py”.
Only default python modules are used.


10- Database Setup
----------------
schema name: serverdata

role/user:
- seeker (admin rights on serverdata schema)
- seeker_ro (read only on serverdata schema)

Access Database Rules:
- At a Network Level the Database engine is setup to deny all network access.

- Data is uploaded by using the admin account “seeker” for the “serverdata” schema.
  This role has no access to any other schemas in the database engine. It is password enabled

- Queries can be done only by logging to the control node and only by using the “read only” role “seeker_ro”.
  This role has access only on the “serverdata” schema. It is password enabled.

- The Postgres DB engine creates a default account of “postgres”. This login needs its own home directory
  but it is configured not to allow for a login session (remote or local). This account is the default admin db account. 
  It is password enabled.


11- Database Tables:
--------------------

- a1servers: Is the main table. It stores general information for the servers.
  The primary key for this table is a unique ID number which is being generated by Ansible.
  This key is being referenced by the other tables to ensure data integrity.
  You may have two hosts with the same hostname but you cannot have two entries with the same unique ID.
  This table stores version of the OS, RAM size, CPU type, cores.

- lvm_setup: Captures how the drives are setup with LVM. Displays which drives belong to which Volume and Logical groups.

- network_interfaces: Captures the interface names their assigned IPs and in what network they belong.

- network_routes: Captures the information from the routing table.

- network_setup: Captures the default interface, default route, interface type and dns entries.

- rpm_packages: Captures all installed RPM packages for each host.

- storage_capacity: Captures all the mount points and options set for each mount for all devices,
  uuid for each mount, disk size/availability/usage.

- external_routes / internal_routes: These contain routes/networks that are used for comparison with current setup of servers.
  Suppose that traffic from server XYZ needs to go out from interface A but instead it goes out from interface B, 
  these tables will allow us to capture such anomalies.

- hpv_vm_invewntory: This captures if a physical server is a KVM HyperVisor and if so what VMs exist in that specific 
  server. This table so far captures only KVM hypervisors.

