# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:11:14 2021

@author: vanwy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'

df = pd.read_csv(URL_DATASET)

print(len(df))

x = df.query('Country == "Brazil"').index

print(len(x))

last = len(x) - 1
lastMinusTwenty = last - 20

print(last, "\t", lastMinusTwenty)

ax = df.Confirmed[x[lastMinusTwenty]:x[last]].plot(kind = 'bar', 
                                   title = 'South Africa = COVID-19 (Confirmed Case)', 
                                   figsize = (15, 10), 
                                   legend = False, 
                                   fontsize = 12)
ax.set_xlabel("Date", fontsize = 12)
ax.set_ylabel("Confirmed Cases", fontsize = 12)
ax.set_xticklabels(df.Date[x[lastMinusTwenty]:x[last]], rotation = 90)
plt.show()

ax = df.Deaths[x[lastMinusTwenty]:x[last]].plot(kind = 'bar', 
                                   title = 'South Africa = COVID-19 (Number of Deaths)', 
                                   figsize = (15, 10), 
                                   legend = False, 
                                   fontsize = 12, 
                                   color = 'red')
ax.set_xlabel("Date", fontsize = 12)
ax.set_ylabel("Number of Deaths", fontsize = 12)
ax.set_xticklabels(df.Date[x[lastMinusTwenty]:x[last]], rotation = 90)
plt.show()