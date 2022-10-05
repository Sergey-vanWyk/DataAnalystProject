# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:30:13 2021

@author: vanwy
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
import sklearn.datasets

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'

df = pd.read_csv(URL_DATASET)
#print(df.info())
df['Date'] = pd.to_datetime(df['Date'])
#print(df.info())

grouped = df.groupby('Country').sum()
print(grouped)
grouped_SA_Death = df[df['Country'] == 'South Africa'].groupby([pd.Grouper(key='Date', axis=0, freq='m')])['Deaths'].mean()
grouped_SA_Recovered = df[df['Country'] == 'US'].groupby([pd.Grouper(key='Date', axis=0, freq='m')])['Deaths'].mean()
print(grouped_SA_Death)
print()
print(grouped_SA_Recovered)

ax = grouped_SA_Recovered.plot(kind ='line', color='red')

grouped_SA_Death.plot(kind ='line',title ='Death by COVID',color='green', ax=ax)
plt.show()

grouped_SA_Death_byYear = df[df['Country'] == 'South Africa'].groupby([pd.Grouper(key='Date', axis=0, freq='y')])['Confirmed'].sum()
grouped_SA_Recovered_byYear = df[df['Country'] == 'US'].groupby([pd.Grouper(key='Date', axis=0, freq='y')])['Confirmed'].sum()
print(grouped_SA_Death_byYear)
print()
print(grouped_SA_Recovered_byYear)

ay = grouped_SA_Recovered_byYear.plot(kind ='bar', color='blue')

grouped_SA_Death_byYear.plot(kind ='bar',title ='Confirmed with Covid',color='yellow', ax=ay)
plt.show()