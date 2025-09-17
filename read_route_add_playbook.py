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



#with open('example-route_table_support-playbook.yml', 'r') as file:
#   playbook_data = yaml.safe_load(file)

var1=routes_config[0]['tasks'][1]

#print(var1)


#This is a dict
route_variables=(var1["vars"])

#print(route_variables['network_connections'])
network_config=route_variables['network_connections'][0]

#interface_name
ifname=network_config['name']

#Contains ip-mode-methods-route
ipinfo=(network_config['ip'])

#Contains routes
routes=ipinfo['route']
print(routes)
for i in routes:
    print(i)





#list_1=[{"var1":"one"},{"var2":"two"},{"var3":"three"}]
#for i in list_1:
#    print(i)


dict_1={
    "var1":"one",
    "var2":"two",
    "var3":"three"
}
#print(dict_1['var1'])
