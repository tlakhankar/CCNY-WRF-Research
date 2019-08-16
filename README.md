# CCNY-WRF-Research

This will be used to keep track of our issues for research under Dr. Tarendra Lakhankar at CCNY. 

## Members:

- Arik Iridisy 
- Kendall Molas
- 


## Overview
This Readme contains an explanation of how to use this GitHub repository and operates as a table of contents for all the documentation written for this project. 

The GitHub repository has two functions. One is to hold any scripts written to either automate workflow or for analysis purposes. The other is to operate as a Project Management system. This is accomplished through the _Issues_ system in GitHub. Each issue functions as an actionable item that can be worked toward. Issues can be given tags, priorities, and  assigned to team members. Issues can have replies further explaining the problem or solution. 

These issues form the build blocks for _Projects_. Projects are a way to organize issues using a Trello Board like system. By default there are 3 columns, _Todo, In Progress, Completed_ however more can be added or removed at your convenience. The issues can be moved across columns using the GUI under the Projects tab. _One issue can be a part of multiple projects_, i.e. Issue #4 can be a card in both Project A and Project B. 



## Docker 

An underlying technology for this entire project is Docker. Docker is a containerization/sandboxing program that allows multiple Linux boxes to be instantiated on one computer. The primary reason we are using Docker is because NCAR/UCAR has produced a Docker Image which has WRF-HYDRO and all its dependncies prebuilt. Docker also operates as our version management/back up system. The main thing that needs to be understood about Docker are Images and Containers. 



More about Docker can be found [here](https://docs.docker.com/get-started/)



----

# OLD README

## Downloading GFS Data

```
wget -r -l1 --no-parent -nc -nd -A "gfs.t00z.pgrb2.0p25.f*" -R "*.idx" [URL] -P /path/to/folder
```

If -P is included in script, files will be downloaded directly to the specific folder.

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
