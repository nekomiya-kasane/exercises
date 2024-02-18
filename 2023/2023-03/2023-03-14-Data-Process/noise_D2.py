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
c1_mean, c1_var = data['Alcohol'].mean(), data['Alcohol'].var()
c1_random_noise = np.random.normal(0, c1_var, data['Alcohol'].shape)
c1_data= data['Alcohol'].values + c1_random_noise
c2_mean, c2_var = data['Ash'].mean(), data['Ash'].var()
c2_random_noise = np.random.normal(0, c2_var, data['Ash'].shape)
c2_data= data['Ash'].values + c2_random_noise
new_data = pd.DataFrame(
    {'Class':data['Class'].values, 'Alcohol':c1_data, 'Ash':c2_data}
)
new_data.to_csv('./data/D2.csv')