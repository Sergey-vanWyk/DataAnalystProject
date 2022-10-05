# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:25:00 2021

@author: vanwy
"""

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

"""
def get_iris_df():
    ds = sklearn.datasets.load_iris()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    

    df['species'] = [code_species_map[c]
                     for c in ds['target']]
    return df

df = get_iris_df()
"""

iris = datasets.load_iris()

x = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components=2)
x_r = pca.fit(x).transform(x)

lda = LinearDiscriminantAnalysis(n_components=2)
x_r2 = lda.fit(x, y).transform(x)

print('PCA explained variance ratio (first two components): %s' 
      % str(pca.explained_variance_ratio_))
print()
print('LDA explained variance ratio (first two components): %s' 
      % str(lda.explained_variance_ratio_))

plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.bar(x_r[y == i, 0], x_r[y == i, 0], alpha =.8, color=color, lw=lw, label=target_name)
plt.legend(loc='best',shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')

plt.show()

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.bar(x_r2[y == i, 0], x_r2[y == i, 0], alpha =.8, color=color, lw=lw, label=target_name)
plt.legend(loc='best',shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')

plt.show()











