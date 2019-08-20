## /bin/bash

###############################################################
# Add this to aliases and name it to allow easy usage such as sc.
# Example:
    # sc [DIROPT][OPTIONS]
###############################################################


## Created by Kendall Molas for the WRF-Hydro Team at CCNY.
## This is a script cleaning tool that allows the ability to make easy changes to a directory

if [ "$#" -eq 0 ]; then
  printf "============================\n"
  printf "Missing arguments! Type ./script_cleaner.sh help\n"
  printf "============================\n"
  exit 1
fi

# Help Prompt for general program
if [ $1 = "help" ]; then
  printf "=======================================\n"
  printf "The script works as follows:\n"
  printf "./script_cleaner.sh [DIROPT] [OPTIONS]\n"
  printf "DIROPT: 1 - Regridding directory \n\t2 - Simulation Directory\n"
  printf "OPTIONS: Type ./script_cleaner.sh [DIROPT] help for more information on the available scripts\n"
  printf "To remove output files from the regridding or simulation directory, type: ./script_cleaner.sh [DIROPT] clean\n"
  printf "=======================================\n"

# If regrid directory chosen
elif [ $1 -eq 1 ]; then
  # Remove files in the regrid directory that was made due to generating weights and regridding.
  if [ $2 = "clean" ]; then
    printf "Removing the following files: *.LDASIN_DOMAIN1 *.LDASIN_DOMAIN1.nc GFS2WRFHydro_weight_bilinear.nc  SCRIP_WRFHydro_bilinear.nc  PET0.RegridWeightGen.Log SCRIP_GFS_bilinear.nc\n"
    rm *.LDASIN_DOMAIN1 *.LDASIN_DOMAIN1.nc GFS2WRFHydro_weight_bilinear.nc  SCRIP_WRFHydro_bilinear.nc  PET0.RegridWeightGen.Log SCRIP_GFS_bilinear.nc 
    exit 1

  # Generating weight behavior
  elif [ $2 = "gen" ]; then
    if [ $3 = "help" ]; then
      printf "=======================================\n"
      printf "Usage: ./script_cleaner.sh 1 sym [OPTION]\n"
      printf "OPTIONS:\n\t1 - Generate weight of file. Uncomment and change directory in command of this script, if path is not the same.
      \t2 - Regrid forcing data located in input_files.\n"
      printf "=======================================\n"
    elif [ $3 -eq 1 ]; then
      # Uncomment to use
      # ncl 'interp_opt="bilinear"' 'srcGridName="[ENTER PATH HERE]"' 'dstGridName="geo_em.d01.nc"' GFS2WRFHydro_generate_weights.ncl
      echo "Path must be specified here"
    elif [ $3 -eq 2 ]; then
      # ncl 'srcFileName="[ENTER PATH HERE]"' 'dstGridName="geo_em.d01.nc"' GFS2WRFHydro_regrid.ncl
      # Uncomment to use
      # mv *.LDASIN_DOMAIN1 "[ENTER PATH HERE]"
      echo "Path must be specified here"
    else
      echo "Invalid input"
    exit 1
    fi

  # Establising Symlinks
  elif [ $2 = "sym" ]; then
    if [ $3 = "help" ]; then 
      echo "3 parameters must exist"
      echo "USAGE: ./script_cleaner.sh 1 sym [START] [END] [PRESSURE LEVEL]"
      printf "START - starting forecast hour\nEND - ending forecast hour\nPRESSURE LEVEL - pressure level of forcing data\n"
      printf "Change directory name below in order for program to be used.\n\n"
    else 
      if [ $3 = "all" ]; then
        # Uncomment to use
        # cp -as $HOME/[ENTER PATH HERE]/* $HOME/[ENTER PATH HERE]
        echo "Path must be specified here"
      elif [ "$#" -eq 5 ]; then
        for i in $(seq -f "%03g" $3 $4)
        do 
          # Uncomment to use
          # cp -as $HOME/Jean\ Data/$5/gfs.t00z.pgrb2.$5.f$i $HOME/Jean\ Data/regrid/input_files/
          echo "Path must be specified here"
        done
      fi
    fi
    exit 1
  
  # Removing Symlinks from input_files
  elif [ $2 = "rsym" ]; then
    printf "Removing symlinks to input_files directory...\n"
    if [ $3 = "help" ]; then
      echo "3 parameters must exist"
      echo "USAGE: ./script_cleaner.sh 1 rsym [START] [END] [PRESSURE LEVEL]"
      printf "START - starting forecast hour\nEND - ending forecast hour\nPRESSURE LEVEL - pressure level of forcing data\n"
      printf "Change directory name below in order for program to be used.\n\n"
    else 
      if [ $3 = "all" ]; then
        # Uncomment to use
        # rm "$HOME/Jean Data/regrid/input_files/*"
        echo "Path must be specified here"
      elif [ "$#" -eq 5 ]; then
        for i in $(seq -f "%03g" $3 $4)
        do 
          #file="gfs.t00z.pgrb2.$5.f$i"
          #rm "/home/docker/Jean Data/regrid/input_files/$file"
          echo "Path must be specified here"
        done
        fi
      fi
    exit 1
  fi

# Simulation directory chosen
elif [ $1 -eq 2 ]; then
  if [ $2 = "clean" ]; then
    printf "Removing the following files: *CHRTOUT_DOMAIN1 *.CHANOBS_DOMAIN1 *.LDASOUT_DOMAIN1 *.RTOUT_DOMAIN1 frxst_pts_out.txt  diag_hydro.00001 diag_hydro.00000 RESTART.*_DOMAIN1\n"
    rm *CHRTOUT_DOMAIN1 *.CHANOBS_DOMAIN1 *.LDASOUT_DOMAIN1 *.RTOUT_DOMAIN1 frxst_pts_out.txt  diag_hydro.00001 diag_hydro.00000 RESTART.*_DOMAIN1
    exit 1
  fi
fi
