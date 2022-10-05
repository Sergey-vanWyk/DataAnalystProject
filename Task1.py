# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:22:03 2021

@author: vanwy
"""
import pandas as pd
from matplotlib import pyplot as plt
import sklearn.datasets

def get_iris_df():
    ds = sklearn.datasets.load_iris()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    

    df['species'] = [code_species_map[c]
                     for c in ds['target']]
    return df

df = get_iris_df()

df.plot(kind='scatter', x = 'petal length (cm)', y = 'petal width (cm)')
anotherDF = df.groupby('species')
anotherDF.plot(kind='scatter', x = 'petal length (cm)', y = 'petal width (cm)')
plt.title('Length vs Width')
print(df)
plt.show()

print(anotherDF)