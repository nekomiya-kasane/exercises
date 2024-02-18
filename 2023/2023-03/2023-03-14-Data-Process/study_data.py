import os 
from copy import deepcopy

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

from sklearn import preprocessing

data = pd.read_csv('./data/wine.data', 
            names=["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash  ", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"],
            sep=','
        )

columns = data.columns
describes = {'name':[], 'mean':[], 'std':[]}
for c in columns:
    describes['name'].append(c)
    describes['mean'].append(data[c].mean())
    describes['std'].append(data[c].std())


pp = PdfPages(f'各个列的盒图.pdf')
for c in columns:
    if not c in ['Class']:
        print(c)
        plt.boxplot(data[c], vert=True, labels=[c])
        plt.title(f'{c}列的盒图')
        pp.savefig()
        plt.close()
pp.close()