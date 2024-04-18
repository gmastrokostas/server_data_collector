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

# -*- coding: utf-8 -*-
# Copyright: (c) 2022, gmastrokostas <gmastrokostas@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#!/bin/bash
kernel_array=()
index_kernel=`grubby --info=ALL | grep '^kernel' | cut -d "/" -f 3 | tr -d '"'`
counter=0
for loop2 in $index_kernel
do
	kernel_array+=($((counter++)) $loop2)
done
#echo ${kernel_array[@]}

array_1=${kernel_array[@]}


for x in $array_1
do

	echo "{ \"changed\": false, \"operating_system\": \"$array_1\" }"
done


