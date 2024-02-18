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
from sklearn.neighbors import LocalOutlierFactor 

data = pd.read_csv('./data/D2.csv')
data = data[['Alcohol', 'Ash']]
clf = LocalOutlierFactor(n_neighbors=2)
y_pred = clf.fit_predict(data)

liers = data[['Alcohol', 'Ash']]
liers['inlierOrOutlier'] = y_pred
print(liers)

pp = PdfPages('LOF方法检测D2数据集异常点检测散点图.pdf')
inlier = liers[liers['inlierOrOutlier']==1]
plt.figure()
plt.scatter(inlier['Alcohol'], inlier['Ash'], c='green', label='Inlier')
outlier = liers[liers['inlierOrOutlier']==-1]
plt.scatter(outlier['Alcohol'], outlier['Ash'], c='red', label='Outlier')
plt.legend()
plt.title('LOF方法检测D2数据集异常点检测散点图')
pp.savefig()
pp.close()