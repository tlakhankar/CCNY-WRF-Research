# CCNY-WRF-Research

This will be used to keep track of our issues for research under Dr. Tarendra Lakhankar at CCNY. 

## Members:

- Arik Iridisy 
- Kendall Molas

## Current Scripts Available

* cleanFiles.sh: This script is located in the regrid directory, and cleans the regridding directory of files: 
```
*.LDASIN_DOMAIN1 *.LDASIN_DOMAIN1.nc GFS2WRFHydro_weight_bilinear.nc  SCRIP_WRFHydro_bilinear.nc  PET0.RegridWeightGen.Log SCRIP_GFS_bilinear.nc 
```
* cleanSimulation.sh: This script is located in the simulation directory, and cleans the simulation directory of files:
```
*CHRTOUT_DOMAIN1 *.CHANOBS_DOMAIN1 *.LDASOUT_DOMAIN1 *.RTOUT_DOMAIN1 frxst_pts_out.txt  diag_hydro.00001 diag_hydro.00000 RESTART.*_DOMAIN1
```
* establish_force_links.sh: This script is located in the simulation directory, and creates a symlink between all files in  regrid/output_files/ and FORCING/
* establish_links.sh: This script is located in the regridding directory, and creates a symlink from a pressure directory [0p25], to regrid/input_files.
* regrid.sh: This script is located in the regridding directory, and allows ability to generate weight or regrid files in input_files. Note that when generating weight, the .f000 file is used.
* remove_links.sh: This script is located in the regridding directory, and removes links from the input_files directory.


Using as a reference until later.
