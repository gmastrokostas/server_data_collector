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

#This class is created to process the data captured by ansible.
import os
import sys

class file_processing:
    #This directory has the csv files ansible creates and fetches with
    #data from the servers
    #servers_path = "/home/seeker/stash/server_data_collector/servers"
    #the csv_file variable will be assigned one of these variables
    #depending what info we pass when we call this class.
    #servers_data_table = "/home/seeker/stash/server_data_collector/datafiles/servers"
    #rpm_data_table = "/home/seeker/stash/server_data_collector/datafiles/rpm_packages"
    #
    def __init__(self, file_type,
                 servers_path,
                 servers_data_table,
                 rpm_data_table,
                 storage_table,
                 network_setup_table,
                 network_interfaces_table,
                 network_routes_table,
                 lvm_setup_table,
                 interface_hardware_info_table):
        
        self.servers_path = servers_path
        self.servers_data_table = servers_data_table
        self.rpm_data_table = rpm_data_table
        self.storage_table = storage_table
        self.network_setup_table = network_setup_table
        self.network_interfaces_table = network_interfaces_table
        self.network_routes_table = network_routes_table
        self.lvm_setup_table = lvm_setup_table
        self.interface_hardware_info_table=interface_hardware_info_table
        

        if file_type == "servers":
           self.csv_file = self.servers_data_table
           self.data_file = "servers.csv"

        elif file_type == "rpm":
            self.csv_file = self.rpm_data_table
            self.data_file = "rpm_packages.csv"

        elif file_type == "storage":
            self.csv_file = self.storage_table
            self.data_file = "storage_capacity.csv"

        elif file_type == "network_setup":
            self.csv_file = self.network_setup_table
            self.data_file = "network_setup.csv"

        elif file_type == "network_interfaces":
            self.csv_file = self.network_interfaces_table
            self.data_file = "network_interfaces.csv"

        elif file_type == "network_routes":
            self.csv_file = self.network_routes_table
            self.data_file = "network_routes.csv"

        elif file_type == "lvm_setup":
            self.csv_file = self.lvm_setup_table
            self.data_file = "lvm_setup.csv"
            
        elif file_type=="interface_hardware_info":
            self.csv_file = self.interface_hardware_info_table
            self.data_file="interface_hardware_info.csv"

    def dataprocessing(self):

        # clear the files in the datafiles directory
        try:
            with open(self.csv_file, 'w') as fw:
                pass
        except:
            return "Trouble clearing the files under the datafile directory"

        # open the files in the datafiles directory for writing
        f_csv_file = open(self.csv_file, 'a+')
        # Find all the csv files for all servers in the servers directory
        for root, dirs, files in os.walk(self.servers_path):
            for x in files:
                 if self.data_file in x:
                    found_file = root + "/" + x
                    ###
                    f_open = open(found_file, 'r')
                    f_csv_file.write(f_open.read())
                    ###
        f_csv_file.close()
