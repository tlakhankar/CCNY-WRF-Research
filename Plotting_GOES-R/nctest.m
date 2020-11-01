ncfile = 'test.nc';
ncinfo(ncfile)
ncdisp(ncfile)
ncid = netcdf.open('test.nc','NC_NOWRITE');
varname = netcdf.inqVar(ncid,0);
varid = netcdf.inqVarID(ncid,varname); 
netcdf.getVar(ncid,varid);
data = netcdf.getVar(ncid,varid);

%Loading Variables into allocated GP-Registers based on Simulank2019b ABI
rain = ncread('test.nc','RRQPE');
%cellMethods = ncreadatt('test.nc','RRQPE','cell_methods')
x = ncread('test.nc','x');
y = ncread('test.nc','y');
dqf =  ncread('test.nc','DQF');
time_bounds = ncread('test.nc','time_bounds');
goes_imager_projection = ncread('test.nc','goes_imager_projection');



%Synthesizing intereim products

perspective_point_height = ncreadatt('test.nc','goes_imager_projection','perspective_point_height')
semi_major_axis = ncreadatt('test.nc','goes_imager_projection','semi_major_axis')
H = perspective_point_height + semi_major_axis
lon_origin = ncreadatt('test.nc','goes_imager_projection','longitude_of_projection_origin')
r_eq = semi_major_axis;
r_pol = ncreadatt('test.nc','goes_imager_projection','semi_minor_axis')

[lat_rad,lon_rad] = meshgrid(x,y);

lambda_0 = (lon_origin*pi)/180.0

a_var = power(sin(lat_rad),2.0) + (power(cos(lat_rad),2.0))* (power(cos(lon_rad),2.0)+(((r_eq*r_eq)/(r_pol*r_pol))*power(sin(lon_rad),2.0)));  
b_var = -2.0*H*cos(lat_rad)*cos(lon_rad);
c_var = (H*H)-(r_eq*r_eq);

disp("r_s")
r_s = (-1.0*b_var - sqrt( (b_var*b_var)-(4.0*a_var*c_var)) )/(2.0*a_var);

disp("s_*")
s_x = r_s*cos(lat_rad)*cos(lon_rad);
s_y = - r_s*sin(lat_rad);
s_z = r_s*cos(lat_rad)*sin(lon_rad);

lat = (180.0/pi)*(atan(((r_eq*r_eq)/(r_pol*r_pol))*((s_z/sqrt(((H-s_x)*(H-s_x))+(s_y*s_y))))));
lon = (lambda_0 - atan(s_y/(H-s_x)))*(180.0/pi);

size(lat)
size(lon)
imagesc(lat,lon,rain) 
axis xy tight


disp("End of Code");