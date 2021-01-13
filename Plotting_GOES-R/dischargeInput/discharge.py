import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot(filename):

    dp = lambda x: pd.datetime.strptime(x,'%Y-%m-%d %H:%M')
    df = pd.read_csv(
        filename,
        sep='\t',
        parse_dates=['datetime'],
        date_parser=dp
    )
    df = df.fillna(0)

    print(df.head())

    # NOTE: Change the title of the graph by changing the `title` parameter's value
    ax = df.plot(x='datetime', y='123892_00060', kind='line',title='USGS 50043800 Rio de La Plata at Comerio, PR')
    df.plot(ax=ax, x='datetime', y='233641_00045', kind='line')
    ax.set(xlabel='Date', ylabel='Discharge (cubic feet per second)')
    ax.legend(['Discharge','Precipitation'])
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot('nwis.waterdata.usgs.govE.tsv') # NOTE: Put the input filename here