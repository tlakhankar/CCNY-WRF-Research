# Regridding

## Overview
Regridding is the process of interpolating from one grid resolution to a different grid resolution. With regridding, it utilizes the geo_em.dXX.nc file made in Step 1, and regrids the data to the specified domain. Where XX is a number such as 00, 01, etc.  NCAR provides regridding scripts that are available to the public and downloadable on their [website](https://ral.ucar.edu/projects/wrf_hydro/regridding-scripts). They provide regridding scripts for 6 different forcing datasets: NLDAS, GLDAS, HRRR, MRMS, GFS, and RAP.

## Forcing Data

There are six forcing datasets that have regridding scripts available to them: NLDAS, GLDAS, HRRR, MRMS, GFS, and RAP.

| ESMF Regridding Script Packages | RAM Required |
| ------------------------------- |:------------:|
| NLDAS                           | 197.89 MB    |
| GLDAS                           | 615.03 MB    |
| HRRR                            | 1342.56 iB   |
| MRMS                            | 15369.06 MB  |
| GFS                             | 729.73 MB    |
| RAP                             | 204.45 MB    |

Currently, the only usable forcing data is: GFS\*. A google sheet is provided [here](https://docs.google.com/spreadsheets/d/1cGk34DqIzk_h-CIn1Qek68_gjVpNiAzbHFf2RAxH-Jo/edit?usp=sharing) which displays which data is feasible for use.

\* GFSANL is the only forcing data that can be used with the GFS regridding script that works properly.

### Downloading Forcing Data

* [NLDAS](https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_FORA0125_H.002/)
* [GLDAS](https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.1/)
* [HRRR](https://www.nco.ncep.noaa.gov/pmb/products/hrrr/)
* [MRMS](https://www.nssl.noaa.gov/projects/mrms/)
* [GFS]( https://nomads.ncep.noaa.gov/)
* [RAP](https://www.nco.ncep.noaa.gov/pmb/products/rap/)

\* GFSANL https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs

## Interpolation Methods

In the regridding scripts there are two available types of interpolation methods: bilinear and conserve. By default, the regrid script uses bilinear for the interpolation method. It utilizes bilinear by default as it is easy to use and applies to when the source and destination are rectlinear. For more information on the interpolation methods, UCAR provides more details [here](https://climatedataguide.ucar.edu/climate-data-tools-and-analysis/regridding-overview).

## Using Regridding Scripts

To regrid the forcing data to a specific domain, the procedure is straightforward with any of the datasets. Some of the commands may differ as the data used are different, look into the READMEs for any of the regridding scripts in order to use them properly.

Before regridding make sure that the geo_em.dXX.nc file is in the same directory as the regridding scripts. Also, a folder name input_files must be made. The folder, input_files, will contain the forcing data downloaded.

GFSANL will be used to demonstrate the process.

### Generating weights

To generate the weights properly, execute the following command:
```
ncl 'interp_opt="bilinear"' 'srcGridName="input_files/gfsanl_4_YYYYMMDD_XXXX_xxx.grb2"' 'dstGridName="geo_em.d01.nc"' GFS2WRFHydro_generate_weights.ncl
```

* YYMMDD: Year, Month, and Day
* XXXX: Model Cycle
* xxx: Output Timestep must be either 003 or 006.

If interpolation method wants to be changed, it can be changed to "conserve".

After weights are generated, regridding is now possible. Execute the following command:

```
ncl 'srcFileName="gfsanl_4*.grb2"' 'dstGridName="geo_em.d01.nc"' GFS2WRFHydro_regrid.ncl
```

If the interpolation method is changed to conserve, an option must be changed in the [FORCING]\_regrid.ncl file. Uncomment wgtFileName_conserve and comment out wgtFileName_bilinear.

## Issues

We have experienced issues using the intentional GFS forcing data which utilizes forecasting hours. Look at the issues tab for more details.
