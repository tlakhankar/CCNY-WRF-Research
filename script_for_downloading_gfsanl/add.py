from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

f = open("myfile.dat",'w')

start_date = date(2016, 1, 1)
end_date = date(2020, 1, 2)
for single_date in daterange(start_date, end_date):
    print(f'https://nomads.ncdc.noaa.gov/data/gfsanl/{single_date.strftime("%Y%m")}/{single_date.strftime("%Y%m%d")}/')
    f.write(f'https://nomads.ncdc.noaa.gov/data/gfsanl/{single_date.strftime("%Y%m")}/{single_date.strftime("%Y%m%d")}/\n')

f.close()