import pandas as pd
import mplfinance as mpf
import os
import urllib.request
import time

share = 'AMZN'
t = round(time.time())
period = float(input('Enter a period (years): '))
url = f'https://query1.finance.yahoo.com/v7/finance/download/{share}?period1={round(t - 31536000 * period)}&period2={t}&interval=1d&events=history&includeAdjustedClose=true'

file_path = os.path.join('data')
os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path, share + '.csv')
urllib.request.urlretrieve(url, csv_path)

df = pd.read_csv(csv_path)
# print(df)
# df.info()

df.Date = pd.to_datetime(df.Date)
# df.info()
df = df.set_index('Date')
# print(df)
plottype = 'candle'
if period > 2:
    plottype = 'line'
# mpf.plot(df, volume=True, tight_layout=True)
# mpf.plot(df, volume=True, type='line', tight_layout=True)
# mpf.plot(df['2021-01'], volume=True, tight_layout=True)
# mpf.plot(df['2021-01':], type='candle', mav=10, volume=True, tight_layout=True)
mpf.plot(df, type=plottype, mav=10, volume=True, tight_layout=True)
