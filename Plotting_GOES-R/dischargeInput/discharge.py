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
    df = df.dropna()

    print(df[['datetime','123955_00065']])
    ax = df.plot(x='datetime', y='123955_00065', kind='line',title='USGS 50043800 Rio de La Plata at Comerio, PR')
    ax.set(xlabel='Date', ylabel='Discharge (cubic feet per second)')
    ax.legend(['Site No. 50043800'])
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot('nwis.waterdata.usgs.govF.tsv')