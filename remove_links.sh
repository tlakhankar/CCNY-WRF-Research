### This script allows the ability to remove symbolic links if any errors were experienced when regridding
#!/bin/bash

if [ "$1" == "r" ]; then
	printf "Removing all files in input directory\n"
	exit 1
else
	if [ "$#" -ne 3 ]; then
		echo "3 parameters must exist"
		echo "USAGE: ./remove_links.sh [START] [END] [PRESSURE LEVEL]"
		exit 1
	fi

	for i in $(seq -f "%03g" $1 $2)
	do 
		file="gfs.t00z.pgrb2.$3.f$i"
		rm "/home/docker/Jean Data/regrid/input_files/$file"
	done
fi
