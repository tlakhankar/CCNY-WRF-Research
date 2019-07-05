### This script allows an easy way to create symbolic links of files.
#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "3 parameters must exist"
	echo "USAGE: ./establish_links.sh [START] [END] [PRESSURE LEVEL]"
fi

for i in $(seq -f "%03g" $1 $2)
do 
	ln -s "~/Jean\ Data/$3/gfs.t00z.pgrb2.$3.f$i" "/home/docker/Jean Data/regrid/input_files"
done
