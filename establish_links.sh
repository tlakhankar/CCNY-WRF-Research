### This script allows an easy way to create symbolic links of files.
#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "3 parameters must exist"
	echo "USAGE: ./establish_links.sh [START] [END] [PRESSURE LEVEL]"
	exit 1
fi

for i in $(seq -f "%03g" $1 $2)
do 
	cp -as $HOME/Jean\ Data/$3/gfs.t00z.pgrb2.$3.f$i $HOME/Jean\ Data/regrid/input_files/
done
