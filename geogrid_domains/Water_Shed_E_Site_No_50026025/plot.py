import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dateparse = lambda x: pd.datetime.strptime(x,'%m/%d/%Y %H:%M')
df = pd.read_csv("nwis.waterdata.usgs.gov.tsv", sep="\t", usecols=['Date', 'Discharge'],date_parser=dateparse)
#df = pd.read_csv('actual_clean2.csv',names=['Date','Discharge'],sep=',',parse_dates=['Date'],date_parser=dateparse)

print(df)
#yData = df["123892_00060"].values
#xData = df["datetime"].values

ax = df.plot(x='Date',y='Discharge',kind='line',title="USGS Discharge Rates for Watershed E")


ax.set(xlabel='Date',ylabel='Discharge Rate (ft^3/s)')
plt.show()
'''
print(xData.size)
print(yData.size)
plt.plot(yData)
'''
'''
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
'''
plt.show()


