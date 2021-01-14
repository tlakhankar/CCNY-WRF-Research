# CCNY-WRF-Research

This will be used to keep track of our issues for research under Dr. Tarendra Lakhankar at CCNY.


## Overview
This Readme contains an explanation of how to use this GitHub repository and operates as a table of contents for all the documentation written for this project.

The GitHub repository has two functions. One is to hold any scripts written to either automate workflow or for analysis purposes. The other is to operate as a Project Management system. This is accomplished through the _Issues_ system in GitHub. Each issue functions as an actionable item that can be worked toward. Issues can be given tags, priorities, and  assigned to team members. Issues can have replies further explaining the problem or solution.

These issues form the build blocks for _Projects_. Projects are a way to organize issues using a Trello Board like system. By default there are 3 columns, _Todo, In Progress, Completed_ however more can be added or removed at your convenience. The issues can be moved across columns using the GUI under the Projects tab. _One issue can be a part of multiple projects_, i.e. Issue #4 can be a card in both Project A and Project B.

## Important File Paths
Location of this repo clones on Anthony's Office Computer
```
 /home/engela/Desktop/ARIK_NO_TOUCHY/CCNY_WRF_RESEARCH
```

## [Docker](https://github.com/WK-M/CCNY-WRF-Research/wiki/Docker)

An underlying technology for this entire project is Docker. Docker is a containerization/sandboxing program that allows multiple Linux boxes to be instantiated on one computer. The primary reason we are using Docker is because NCAR/UCAR has produced a Docker Image which has WRF-HYDRO and all its dependencies prebuilt. Docker also operates as our version management/back up system. The main thing that needs to be understood about Docker are Images and Containers.



More about Docker can be found [here](https://docs.docker.com/get-started/)


## [Regridding](https://github.com/WK-M/CCNY-WRF-Research/wiki/Regridding-and-Forcing)

Regridding is the process of interpolating from one grid resolution to a different grid resolution. With regridding, it utilizes the geo_em.dXX.nc file made in Step 1, and regrids the data to the specified domain. Where XX is a number such as 00, 01, etc.  NCAR provides regridding scripts that are available to the public and downloadable on their [website](https://ral.ucar.edu/projects/wrf_hydro/regridding-scripts). They provide regridding scripts for 6 different forcing datasets: NLDAS, GLDAS, HRRR, MRMS, GFS, and RAP.

## Directories
- `/geogrid_domains`
   - Contains the input and output for each domain to be simulated in WRF-Hydro.
   - The directory name provides the watershed letter designation used for the project, and the USGS gage number in that watershed
      - `WATERSHEF_<NAME>_Site_No_<USGS_SITE#>`
   - The `.nc` files required for the `/DOMAIN` and `/FORCING` directories for the sim can be found here.
   - The NWS/USGS Gauge data for the watershed location can also be found here
   - A MAP provided by USGS for the gage and its location is also provided

- `/R_Script`
   - Contians the R script provided by NCAR to create the wrf_input files
   - Refer to the `README.txt` in these folders

- `/ref`
   - Old reference files, has some notes on the namelist file settings
