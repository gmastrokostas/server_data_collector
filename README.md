# server_data_collector  v 0.4

#IMPORTANT PLEASE READ
This is the core release. It does not contain the features I am currently working on.
This release serves as a starting point in order to keep building on top of it.
To get things rolling sort to speak.
For a full list of all the items I am working on see the "To Do" section.

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
-------- 
Do quick queries  for data server setup information.


Summary of how it works:
-----------------------
A single control node is capturing server data through the use of ansible and ansible facts.
The data is brought back to the control node and uploaded on the database which runs on.
None of the remote servers interact with the database. As a result there is no need to setup
sql clients on the servers nor do you have to setup special access rules for the network or for
the database. The database has referential releationships.

Few examples of data captured. See "Data Captured" section for full list
--------------------------------------------------------------------------   
	\ RPM Packages installed
	\ Distro release
	\ Server Brand
	\ CPU Info
	\ RAM and SWAP info
	\ Mount points
	\ Default Routes
	\ etc.


2- Tools used to capture data:
--------------------------
 - Ansible v 2.9
 - Database Setup
Postgres Database v 14


3- Server Requirements:
--------------------
OS: Centos8 - Rocky8 - Currently being tested in RedHat 8

CPU: 1GhZ

RAM: 2GB RAM


4- Logical Diagram of how Data is captured and stored:
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
                           |
                           v
     -------------  -------------   -------------  -------------   
     |  server   |  |  server   |   |   server  |  |   server  |
     ------------   -------------   -------------  -------------




5- Database Setup
--------------
Type: PostgreSQL
Version: 14
role: seeker (superuser)
db_name: serverdata with owner seeker
schema_name: serverdata_schema



6- Database Tables
----------------
- serverdata_schema.servers
- serverdata_schema.command_line_options
serverdata_schema.hpv_vm_inventory
serverdata_schema.network_setup
serverdata_schema.rpm_packages
serverdata_schema.rpm_packages_pre
serverdata_schema.storage_capacity



7- Data Captured - All data are marked with the ansible timestamp fact:
--------------
Table "servers" (This is the main table):
	hostname
	Operating System and Release
	SELinux Status/mode/type
	Total RAM
	CPU Brand / Cores / arch
	Server Brand
	Virtualization role and what type
	uptime

Table "hpv_vm_inventory":
	hostname
	name of virtual machine

Table "networ_setup":
	hostname
	default route
	default interface
	interface type
	dns entries
	
Table "rpm_packages"
	hostname
	rpm name
	rpm version
	rpm release

Table "Storage setup"
	hostname
	mount points
	device
	blocks available / total / used
	mount options
	uuid
	swap mount / total / free

Table "command line options"
	hostname
	command line options

	
8- To Do (subject to constant change):
---------
8a- Additional features to be added
Add functionality to enable comparison of setup between dates.
  Example:
   * Any changes on rpm (installs, updates).
   * Any changes on mount points, routing tables, etc
   * Historical data comparison for storage /memory usage etc.

8b- Additional Data to be captured:
- Routing Tables
- LVM information (pvs /vgs/ lvs)
- Match IPs with their respective interfaces. Most likely a custom ansible module is needed.
- Extend the information for the VMs. There are limitations with the ansible module. Most likely you will have 
  to create a custom ansible module.
- Add a table called "Performance Setup" to have performance relate configurations. SAR data

8c- Database configuration:
- Create an auto increamental ID key to use as your primary key, instead of hostname
- Create custom views
- Possibly needed triggers to enable the database to pick up any changes being made -- see 8a-
