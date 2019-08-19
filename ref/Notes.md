Some quick notes on namelist.hrldas and hydro.namelist.

Dependent variables in namelist.hrldas:

- START_YEAR  : Start year of forcing data
- START_MONTH : Start month of forcing data
- START_DAY   : Start day of forcing data
- START_HOUR  : Start hour of forcing data
- START_MIN   : Start minute of forcing data
- KHOUR       : Number of hours that you will run the file for.
- FORCING_TIMESTEP\*  : Based on model cycle or interval of forecast hour (in seconds)
- NOAH_TIMESTEP\*     : Based on model cycle or interval of forecast hour (in seconds)

Dependent variables in hydro.namelist:

- out_dt\*      : Based on model cycle or interval of forecast hour

To plot the discharge rate enable the frxst_pts_out variable in hydro.namelist.

\* These must be the same. If FORCING_TIMESTEP = 3600, then out_dt must be 60. (in minutes)

Notable issues:

- Regridding sometimes results in getting a day 32 output file which is not possible. More information about this issue is located [here](https://github.com/WK-M/CCNY-WRF-Research/issues/21)

