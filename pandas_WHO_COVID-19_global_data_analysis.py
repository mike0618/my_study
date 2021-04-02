import numpy as np
import pandas as pd
import os
import urllib.request

url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
file_path = os.path.join('data', 'covid')

os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path, 'WHO-COVID-19-global-data.csv')
urllib.request.urlretrieve(url, csv_path)

df = pd.read_csv(csv_path)
df_index = df.index
df_cols = df.columns
print(df)
print(df_index)
print(df_cols)
print(df_index.values)
print(df.values)
print(df.dtypes)
print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.Country)
print(df.Country.unique())
print(df.loc[1:5, 'Country'])
print(df.loc[1:8, ['Country', 'New_cases']])
print(df.Country == 'United States of America')
print(df[df.Country == 'United States of America'])
print(df[df.New_deaths > 1000])
print(df.loc[df.New_deaths > 1000, ['New_deaths', 'Country']])
print(df.loc[(df.New_deaths > 1000) & (df.Country_code == 'US'), ['Date_reported', 'Country', 'New_cases', 'New_deaths', 'Cumulative_deaths']])
print(df.loc[df.Country_code == 'US', ['New_cases']].max())
print(df.loc[df.Country_code == 'US', ['New_cases']].min())
print(df.loc[df.Country_code == 'US', ['New_cases']].sum())
print(df.loc[df.Country_code == 'US', ['New_deaths']].sum())
print(df.loc[df.Country_code == 'US', ['Cumulative_deaths']].max())
print(df.New_deaths.idxmax())
print(df.loc[df.New_deaths.idxmax(), ['Date_reported', 'Country', 'New_cases', 'New_deaths', 'Cumulative_deaths']])
print(df[df.New_deaths < 0])
df['pct_cases'] = (df['New_cases'] / df['Cumulative_cases']) * 100
print(df)
