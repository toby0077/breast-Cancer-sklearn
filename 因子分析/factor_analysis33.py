# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:32:12 2018
@author: Administrator

pca =PCA(n_components='mle')报错
 elif n_components >= 1 and n_components < .8 * min(X.shape):

TypeError: '>=' not supported between instances of 'str' and 'int'
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA

cancer=load_breast_cancer()
pca =PCA(n_components=0.98)
#pca= PCA(n_components='mle')  

digits = load_breast_cancer()
X_digits = cancer.data
y_digits = digits.target

# Plot the PCA spectrum
pca.fit(X_digits)
print (pca.explained_variance_ratio_)
print (pca.explained_variance_)
print (pca.n_components_)

#计算协方差
pca.get_covariance()
#Estimated precision of data.计算数据估计的准确性
pca.get_precision()

'''
返回模型参数
{'copy': True,
 'iterated_power': 'auto',
 'n_components': 0.98,
 'random_state': None,
 'svd_solver': 'auto',
 'tol': 0.0,
 'whiten': False}
'''
pca.get_params(deep=True)
#返回降维后的数据
new_data=pca.fit_transform(X_digits)
#返回原始数据,测试结果和原始数据不一致
origin_data=pca.inverse_transform(new_data)




