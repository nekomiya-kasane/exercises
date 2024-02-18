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
use_cols = ["Alcohol", "Malic acid", "Ash", "Alcalinity of ash  "]

# 等距离散化
k = 5
d1 = pd.cut(data[use_cols[0]], k, labels=range(k))
data[use_cols[0]] = d1

# 信息增益离散化
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
import re 
t = DecisionTreeRegressor(max_depth=2).fit(data[use_cols[1]].values.reshape(-1, 1), data['Class'])
text_representation = tree.export_text(t)
cuts = []
for line in text_representation.split('\n'):
    if 'feature_0' in line:
        cuts.append(float(re.findall(r"\d+\.?\d*", line)[1]))
cuts = list(set(cuts))
cuts.sort()
cuts = [data[use_cols[1]].min()] + cuts + [data[use_cols[1]].max()]
d2 = pd.cut(data[use_cols[1]], cuts, labels=range(len(cuts)-1))
data[use_cols[1]] = d2

# 卡方离散化
import numpy as np 
from sklearn.preprocessing import KBinsDiscretizer
est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans') 
est.fit(data[use_cols[2]].values.reshape(-1, 1))
d3 = est.transform(data[use_cols[2]].values.reshape(-1, 1))
data[use_cols[2]] = d3

# CAIM 离散化
min_val = data[use_cols[3]].min() 
max_val = data[use_cols[3]].max()
interval = (max_val - min_val)/4
discrete_val = [] 
for i in range(len(data[use_cols[3]])): 
    if data[use_cols[3]][i] <= min_val + interval: 
        discrete_val.append(1) 
    elif data[use_cols[3]][i] > min_val + interval and data[use_cols[3]][i] <= min_val + 2*interval: 
        discrete_val.append(2) 
    elif data[use_cols[3]][i] > min_val + 2*interval and data[use_cols[3]][i] <= min_val + 3*interval: 
        discrete_val.append(3) 
    else: 
        discrete_val.append(4)
data[use_cols[3]] = np.array(discrete_val)

data.to_csv('./data/D1-discrete.csv')