#This file is part of server data collector.
#Copyright (C) 2022 - George Mastrokostas
#email: gmastrokostas@gmail.com

#server data collector is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#########################################################################

#!/bin/bash
ping -c 1 127.0.0.1 > /dev/null 2>/dev/null
if [ $? == 0 ];
	then
	echo "{\"changed\": true, \"rc\": 0}"
	else
	echo "{\"failed\": true, \"msg\": \"failed to ping\", \"rc\": 1}"
fi

