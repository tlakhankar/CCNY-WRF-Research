### This script allows the ability to remove symbolic links if any errors were experienced when regridding

#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "3 parameters must exist"
	echo "USAGE: ./remove_links.sh [START] [END] [PRESSURE LEVEL]"
fi

for i in $(seq -f "%03g" $1 $2)
do 
	rm "/home/docker/Jean\ Files/input_files/gfs.t00z.pgrb2.$3.f$i"
done
