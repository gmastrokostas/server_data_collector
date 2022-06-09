# server_data_collector  v 0.4

Purpose:
-------- 
Through the use of SSH collect various data from servers to allow for quick queries about their setup.
This is an agentless setup.
Few examples of data captured are:  
	\ RPM Packages installed
	\ Distro release
	\ Server Brand
	\ CPU Info
	\ RAM and SWAP info
	\ Mount points
	\ Default Routes
	\ etc.


Tools used to capture data:
--------------------------
 - Ansible
 - Postgres Database


Server Requirements:
--------------------
OS: Centos8 - Rocky8 - Currently being tested in RedHat 8
CPU: 1GhZ
RAM: 2GB RAM


Logical Diagram of how Data is captured and stored:
---------------------------------------------------

                   Single Control node
           ------------------------------------
          |     ----------------------------  |
          |     Data is uploaded in Database  |
          |     ----------------------------  |
          |                 ∧                 |
          |     ---------------------------   |
          |     Data is stored in CVS files   |
          |     ---------------------------   |
          |                 ∧                 |
          |     +---------------------------+ |          
          |     Ansible captures server data  |
	  |     +---------------------------+ |
           -----------------------------------
                           ∧
                           |
                           v
     -----------------------------------------------   
     |              |                |             |
+-----------+  +-----------+   +-----------+  +-----------+           
|  server   |  |  server   |   |   server  |  |   server  |
+-----------+  +-----------+   +-----------+  +-----------+
