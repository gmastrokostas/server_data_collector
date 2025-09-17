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

import yaml

with open('example-route_table_support-playbook.yml', 'r') as file:
    routes_config=yaml.safe_load(file)

#print(routes_config[0])

tasks=routes_config[0]['tasks'][1]

discovery=tasks["vars"]["network_connections"]

total_interfaces=len(discovery)

counter=0
while counter < total_interfaces:
    print(discovery[counter])
    counter=counter+1




routes=(discovery[0]['ip']['route'])




#print(var1)
#This is a dict
route_variables=(tasks["vars"])
#print(route_variables['network_connections'])
network_config=route_variables['network_connections'][0]
#interface_name
ifname=network_config['name']
#Contains ip-mode-methods-route
ipinfo=(network_config['ip'])
#Contains routes
routes=ipinfo['route']


