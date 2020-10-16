import netCDF4
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def main():
    nc = netCDF4.Dataset('/GOES_files/test.nc')
    obs_arr = nc.variables['obs_arr'][:,:]
    hdr_typ = netCDF4.chartostring(nc.variables['hdr_typ'][:,:])
    hdr_sid = netCDF4.chartostring(nc.variables['hdr_sid'][:,:])
    hdr_vld = netCDF4.chartostring(nc.variables['hdr_vld'][:,:])
    obs_qty = netCDF4.chartostring(nc.variables['obs_qty'][:,:])
    hdr_arr = nc.variables['hdr_arr'][:,:]

    # the station index
    id=int8(obs_arr[:,0])

    # make a dictionary with each column of information
    d={}
    d['station_id']  = hdr_sid[id]
    d['lon'] = hdr_arr[id,0]
    d['lat'] = hdr_arr[id,1]
    d['elev'] = hdr_arr[id,2]
    d['time'] = hdr_vld[id]
    d['grib_code'] = obs_arr[:,1]
    d['press'] = obs_arr[:,2]
    d['height'] = obs_arr[:,3]
    d['obs_val'] = obs_arr[:,4]
    d['quality'] = obs_qty[:]

    # convert dictionary to dataframe
    df = pd.DataFrame(d)

    # take a look at the first record
    print df.ix[0]



main()