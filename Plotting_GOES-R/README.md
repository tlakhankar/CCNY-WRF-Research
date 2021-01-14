# Purpose

This directory contains all of the files used in plotting percipitation data from the GOES-R dataset against discharge data measured by the USGS gauges. The purpose here is to compare the two values to validate the GOES-R data. Down the line the goal is to also add the simulation output from WRF-HYDRO to the plot to compare all three.

# Current Roadblock
Unable to obtain the rainfall value given a fixed lat-long coordinate. Each `.nc` file is one timestep, and in each timestep the rainfall or RRQPE value needs to be obtianed at a specified lat-long. Due to the different coordinate/projection system used by the GOES-R satalite the data needs to be transformed from radians to lat/long. In this process it becomes impossible to access the RRPQE values through lat/long values. The code based the script is based off also converts everything to  `np.masked.array` which makes it difficult to get the raw data.

The closest we've been able to get is to restrict the lat long that is being plotting on the geo-spatial plot. This is seen in the file `goes_16_data_demo.png`

# Directories/Files

- `/dischargeInput`
    - Plot the USGS gage discharge data
    - discharge.py - Python Script that will generate plot
        - Requires the NumPy, Pandas, and MatPlotLib Python extensions
        - Input, a nwis.waterdata.usgs tsv(tab seperated file)
            - How to obtain this files is found [here:PLACEHOLDER](PLACEHOLDER)
        - Output, a png of the plot
    - frxst_ots_out.csv
        - Output files from WRF-HYDRO Simulations

- `/GOES_files`
    - Directory to store the input `*.nc` files for plotting
    - The GOES-R files themselves are NOT stored on GitHub due to their size, they can be found on the external hard drives.

- `usingPyForGOESR.py`
    - This file is based of the tutorials found [here](https://makersportal.com/blog/2019/7/8/satellite-imagery-analysis-in-python-part-i-goes-16-data-netcdf-files-and-the-basemap-toolkit) and [here](https://makersportal.com/blog/2018/11/25/goes-r-satellite-latitude-and-longitude-grid-projection-algorithm)
    - Input : GOES-R .nc files from `/GOES_files`
    - Desired Output: A plot of the RRQPE (Rainfall) data at a given lattitude-longitude coordinate.

- `usingPandasGOESR.py`
    - Same goal as `usingPyForGOESR.py` but an attempt from scratch using Pandas.

-nctest.m
    - MATLAB file to acomplish the same goals. Moved to python since there were more tutorials. Had the same issue of not being able to access a lat/long's value.