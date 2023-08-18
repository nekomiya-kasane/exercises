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
stand_cols = [c for c in data.columns if c not in ['Class']]

# z_score
z_score_data = deepcopy(data)
zscore_scaler = preprocessing.StandardScaler()
z_score_data[stand_cols] = zscore_scaler.fit_transform(z_score_data[stand_cols])
z_score_data.to_csv('./data/D1-zscore.csv')

# min-max
min_max_data = deepcopy(data)
minmax_scaler = preprocessing.MinMaxScaler()
min_max_data[stand_cols] = minmax_scaler.fit_transform(min_max_data[stand_cols])
min_max_data.to_csv('./data/D1-minmax.csv')

# 十进制小数定标
float_data = deepcopy(data)
maxabs_scaler = preprocessing.MaxAbsScaler()
float_data[stand_cols] = maxabs_scaler.fit_transform(float_data[stand_cols])
float_data.to_csv('./data/D1-float.csv')

# logistic 方法
log_data = deepcopy(data)
log_data[stand_cols] = 1/(np.exp(-log_data[stand_cols].values)+1)
log_data.to_csv('./data/D1-log.csv')