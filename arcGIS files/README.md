# Creating domain files for wrf-hydro using ArcGIS

1. Use the WPS installation on either the middle computer or the computer at the far end in room ST183 to create a geogrid file called geo_em.d01.nc file. To do that login into the ubuntu install on the computer and navigate to the WPS folder located in the ARIK_NO_TOUCHY folder and locate a file called namelist.wps. [Here](../namelist.wps) is an example namelist.wps In that file there are a few variables that need to be changed. After updating these variables, run "geogrid,exe" to create the geogrid file.
	- start_date is the start date of the simulation
	- end_date is the end date of the simulation
	- interval_seconds is the interval time of the forcing data (for gfsanl its 21600)
	- e_we is the horizontal bounds 
	- e_sn is the vertical bounds
	- ref_lat is the center latitude of your bounds
	- ref_lon is the center longitude of your bounds
	- truelat1 should be ref_lat truncated to be an integer
	- truelat2 is left blank
	- stand_lon should be the same as ref_lon
	- geog_data_path is the absolute path to the WPS_GEOG folder (should be somewhere around the WPS folder)
2. Use the create geogrid file with the R script [here](../R_script) to create a wrfinput file. Use "./create_wrfinput.R --geogrid='geo_em.d01.nc' --filltyp=3 --laimo=8" to make it.
3. Import the wrf_hydro_arcgis_preprocessor-5.1.1 folder into the catalog tree in ArcGIS.
4. Use [this step-by-step video](https://www.youtube.com/watch?v=yaaKYNhhCbA) to create the the domain files needed to run wrf-hydro. Make sure to use the created geogrid file. When doing the Process GEOGRID File make sure to use the pr_frxst_pts_csv.csv file for the Forcast Points and the elevation data in the NHDPlusCI folder for Input Elevation Raster. Also make sure to check Create reach-based routing and Create lake parameter. The rest of the options can be left as is. The output zip file should contain all the domain files needed to run wrf-hydro. These files can be found on the 5TB external hard drive
