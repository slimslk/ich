#!/bin/bash

iterations=10

for ((i=1; i<=$iterations; i++))
do
	echo "$(date +"%T") $(ps -e | wc -l)"
#	sleep(5)
done

cat /proc/cpuinfo > processor_info.txt
cat /etc/os-release | grep -w 'NAME=' > os_info.txt
cat os_info.txt | awk -F "=" '{print $2}' > os_name.txt

for j in {50..100}
do
	touch "$j.txt"
done
