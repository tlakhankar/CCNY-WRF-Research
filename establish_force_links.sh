# Located in SIMULATION Directory
# /bin/bash
# This script is to link the files from the output_files directory to the FORCING directory 

if [ "$#" -eq 1 ]; then
	if [ $1 == "-h" ]; then
		printf "This script is to link the files from the output_files directory to the FORCING directory\n"
		printf "USAGE: ./establish_forcing_links.sh [ARG]\n"
		printf "ARG = 1: establish sym links from output_files directory\n"
		printf "ARG = 2: clear out FORCING directory\n"
		exit 1
	elif [[ "$1" -eq 1 ]]; then
		cp -as $HOME/Jean\ Data/regrid/output_files/* "/home/docker/Jean Data/SIMULATION/FORCING/"
	elif [[ "$1" -eq 2 ]]; then
		printf "Files from the Forcing Directory have been removed\n"
		rm /home/docker/Jean\ Data/SIMULATION/FORCING/*
	fi
else
	printf "Type ./establish_force_links.sh -h\n"
fi
