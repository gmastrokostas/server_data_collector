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


