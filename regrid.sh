if [[ "$1" -eq 1 ]]; then
	ncl 'interp_opt="bilinear"' 'srcGridName="/home/docker/Jean Data/0p25/gfs.t00z.pgrb2.0p25.f000"' 'dstGridName="geo_em.d01.nc"' GFS2WRFHydro_generate_weights.ncl
elif [[ "$1" -eq 2 ]]; then
	ncl 'srcFileName="gfs.*.pgrb2.0p25.*"' 'dstGridName="geo_em.d01.nc"' GFS2WRFHydro_regrid.ncl
	printf "================================\n"
	mv *.LDASIN_DOMAIN1 "/home/docker/Jean Data/regrid/output_files"
else
	printf "USAGE: ./regrid.sh [ARG]\n"
	printf "ARG = 1: generate weight\n"
	printf "ARG = 2: regrid\n"
	exit 1
fi
