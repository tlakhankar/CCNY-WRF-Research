from netCDF4 import Dataset
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import os

def lat_lon_reproj(nc_folder):
    os.chdir(nc_folder)
    full_direc = os.listdir()
    nc_files = [ii for ii in full_direc if ii.endswith('.nc')]
    g16_data_file = nc_files[0] # select .nc file
    print(nc_files[0]) # print file name

    # designate dataset
    g16nc = Dataset(g16_data_file, 'r')
    var_names = [ii for ii in g16nc.variables]
    var_name = var_names[0]

    # GOES-R projection info and retrieving relevant constants
    proj_info = g16nc.variables['goes_imager_projection']
    lon_origin = proj_info.longitude_of_projection_origin
    H = proj_info.perspective_point_height+proj_info.semi_major_axis
    r_eq = proj_info.semi_major_axis
    r_pol = proj_info.semi_minor_axis

    # grid info
    lat_rad_1d = g16nc.variables['x'][:]
    lon_rad_1d = g16nc.variables['y'][:]
    
    # close file when finished
    g16nc.close()
    g16nc = None

    # create meshgrid filled with radian angles
    lat_rad,lon_rad = np.meshgrid(lat_rad_1d,lon_rad_1d)

    # lat/lon calc routine from satellite radian angle vectors

    lambda_0 = (lon_origin*np.pi)/180.0

    a_var = np.power(np.sin(lat_rad),2.0) + (np.power(np.cos(lat_rad),2.0)*(np.power(np.cos(lon_rad),2.0)+(((r_eq*r_eq)/(r_pol*r_pol))*np.power(np.sin(lon_rad),2.0))))
    b_var = -2.0*H*np.cos(lat_rad)*np.cos(lon_rad)
    c_var = (H**2.0)-(r_eq**2.0)

    r_s = (-1.0*b_var - np.sqrt((b_var**2)-(4.0*a_var*c_var)))/(2.0*a_var)

    s_x = r_s*np.cos(lat_rad)*np.cos(lon_rad)
    s_y = - r_s*np.sin(lat_rad)
    s_z = r_s*np.cos(lat_rad)*np.sin(lon_rad)

    # latitude and longitude projection for plotting data on traditional lat/lon maps
    lat = (180.0/np.pi)*(np.arctan(((r_eq*r_eq)/(r_pol*r_pol))*((s_z/np.sqrt(((H-s_x)*(H-s_x))+(s_y*s_y))))))
    lon = (lambda_0 - np.arctan(s_y/(H-s_x)))*(180.0/np.pi)

    os.chdir('../')

    return lon,lat

def data_grab(nc_folder,nc_indx):
    os.chdir(nc_folder)
    full_direc = os.listdir()
    nc_files = [ii for ii in full_direc if ii.endswith('.nc')]
    g16_data_file = nc_files[nc_indx] # select .nc file
    print(nc_files[nc_indx]) # print file name

    # designate dataset
    g16nc = Dataset(g16_data_file, 'r')
    var_names = [ii for ii in g16nc.variables]
    var_name = var_names[0]

    # data info    
    data = g16nc.variables[var_name][:]
    data_units = g16nc.variables[var_name].units
    data_time_grab = ((g16nc.time_coverage_end).replace('T',' ')).replace('Z','')
    data_long_name = g16nc.variables[var_name].long_name
    
    # close file when finished
    g16nc.close()
    g16nc = None

    os.chdir('../')
    # print test coordinates
    '''
    f = open("poop2.txt","a")
    for i in range(0,5424):
        for j in range(0,5424):
            print(f"i,j = {i},{j}  ::  {lat[i,j]} N, {abs(lon[i,j])} W", file=f )
    
    f.close()
    '''

    print('{} N, {} W'.format(lat[418,1849],abs(lon[418,1849])))

    return data,data_units,data_time_grab,data_long_name,var_name

nc_folder = "./GOES_files/" # define folder where .nc files are located
lon,lat = lat_lon_reproj(nc_folder)

file_indx = 0 # be sure to pick the correct file. Make sure the file is not too big either,
# some of the bands create large files (stick to band 7-16)

data,data_units,data_time_grab,data_long_name,var_name = data_grab(nc_folder,file_indx)
# main data grab from function above

data_bounds = np.where(data.data!=65535)
#Returns the rows and cols (x,y) in a tuple where the cond is satisfied
# Each element in the tuple is itself a tuple of an array of vals and the dtype
goodData2 = np.extract(data.data!=65535,data)
print(f"Data Bounds = {data_bounds}")
bbox = [np.min(lon[data_bounds]),
        np.min(lat[data_bounds]),
        np.max(lon[data_bounds]),
        np.max(lat[data_bounds])] # set bounds for plotting
# bbox = [-65,17,-68,19]
dimLimit = 5424
goodData = np.full((dimLimit,dimLimit), np.inf)
xBounds = data_bounds[0]
yBounds = data_bounds[1]

val = (lon[data_bounds])

print(f"xBounds Vals = {xBounds}")
print(f"lat = {lat.data}")
print(f"dataShape = {data.shape}")
print(f"data = {data.data}")


#NOTE: Mapping x |--> data_bounds[x] = i |--> lat[i]
# Get the x,y for lat
xForLats = []
yForLats = []
for i in range(0,len(lat)):
    #print(f"xBounds[i] = {xBounds[i]}")
    #print(f" lat[xBounds[i]]: {lat.data[xBounds[i]]}")
    latVal = lat.data[xBounds[i]]
    lonVal = lon.data[xBounds[i]]
    print(f"latval = {latVal}")
    if latVal > 17  and latVal < 19:
        xForLats.append(i)
    if lonVal > -68 and lonVal < -65:
        yForLats.append(i)

print(f"xForLats = {xForLats}")
print(f"yForLats = {yForLats}")
exit()
# TODO: Access at [xBounds[i]][yBounds[i]]
for i in range(0,len(xBounds)):
    x = xBounds[i]
    y = yBounds[i]
    goodData[x][y] = data[x][y] 

    # print(f"x,y, iter = ({x},{y}) {iterCount}")

print(f"Post Loop, iterCount = {iterCount}")
print(goodData)
'''
print(f"Size of size of lon is {lon.shape}")
print(f"Lon is == {lon.data}")

print(f"Size of size of lat is {lat.shape}")
print(f"Lat is == {lat.data}")

print(f"Size of size of  data is {data.shape}")
print(f"LOOK:::Data is == {np.ma.getdata(data)}") #=== print(data.data)
print(f"Type of Data is {type(data)}" )

#print(f"Shape of data_bounds is {data_bounds.shape}")
print(f"Data is == {data_bounds}")
'''
exit()
# figure routine for visualization
fig = plt.figure(figsize=(9,4),dpi=200)

n_add = 0 # for zooming in and out
m = Basemap(llcrnrlon=bbox[0]-n_add,llcrnrlat=bbox[1]-n_add,urcrnrlon=bbox[2]+n_add,urcrnrlat=bbox[3]+n_add,resolution='i', projection='cyl')
m.fillcontinents(color='#d9b38c',lake_color='#bdd5d5',zorder=1) # continent colors
m.drawmapboundary(fill_color='#bdd5d5',zorder=0) # ocean color
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.25)
m.drawstates(zorder=2)
m.pcolormesh(lon.data, lat.data, data, latlon=True,zorder=999,alpha=0.05) # plotting actual RRQPE data
parallels = np.linspace(bbox[1],bbox[3],5)
m.drawparallels(parallels,labels=[True,False,False,False],zorder=2,fontsize=8)
meridians = np.linspace(bbox[0],bbox[2],5)
m.drawmeridians(meridians,labels=[False,False,False,True],zorder=1,fontsize=8)
cb = m.colorbar()

data_units = ((data_units.replace('-','^{-')).replace('1','1}')).replace('2','2}')
plt.rc('text', usetex=True)
#cb.set_label(r'%s $ \left[ \mathrm \right] $'% (var_name,data_units))
plt.title(' on '.format(data_long_name,data_time_grab))
plt.tight_layout()

plt.savefig('goes_16_data_demo.png',dpi=200,facecolor=[252/255,252/255,252/255]) # uncomment to save figure
plt.show()