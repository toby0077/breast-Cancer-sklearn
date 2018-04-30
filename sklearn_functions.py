# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:40:50 2018

@author: Administrator
"""
#绘图
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

#数据预处理
#标准化
#异常值处理
#非线性转换
#二值化
#独热编码（one-hot）
#缺失值插补：支持均值、中位数、众数、特定值插补、多重插补
#衍生变量生成

#模型优化
#不具体列出函数，只说明提供的功能
#特征选择
#随机梯度方法
#交叉验证
#参数调优
#模型评估：支持准确率、召回率、AUC等计算，ROC,损失函数等作图

 #导入测试数据
from sklearn import datasets
#数据预处理
from sklearn.preprocessing import Imputer
#用于训练数据和测试数据分类
from sklearn.cross_validation import train_test_split
#导入数据预处理，包括标准化处理或正则处理
from sklearn import preprocessing
#过渡拟合校验
from sklearn.learning_curve import learning_curve
#样本平均测试，评分更加
from sklearn.cross_validation import cross_val_score


#A回归算法
#最小二乘回归（OLS）
from sklearn import linear_model
reg = linear_model.LinearRegression()
#岭回归
from sklearn import linear_model
reg = linear_model.Ridge (alpha = .5)
#逻辑回归算法
from sklearn.linear_model import LogisticRegression
clf_l1_LR = LogisticRegression(C=C, penalty='l1', tol=0.01)
#核岭回归（Kernel ridge regression）
from sklearn.kernel_ridge import KernelRidge
KernelRidge(kernel='rbf', alpha=0.1, gamma=10)
#套索回归（Lasso）
from sklearn import linear_model
reg = linear_model.Lasso(alpha = 0.1)
#弹性网络回归（Elastic Net）
from sklearn.linear_model import ElasticNet
regr = ElasticNet(random_state=0)
#贝叶斯回归（Bayesian Regression）
from sklearn import linear_model
reg = linear_model.BayesianRidge()
#多项式回归（Polynomial regression——多项式基函数回归）
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
poly.fit_transform(X)
#偏最小二乘回归（PLS）
from sklearn.cross_decomposition import PLSCanonical
PLSCanonical(algorithm='nipals', copy=True, max_iter=500, n_components=2,scale=True, tol=1e-06)
#典型相关分析（CCA）
from sklearn.cross_decomposition import CCA
cca = CCA(n_components=2)



#B聚类分析
#KNN算法
from sklearn.neighbors import KNeighborsClassifier
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
#Kmeans算法
from sklearn.cluster import KMeans
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
#层次聚类（Hierarchical clustering）——支持多种距离
from sklearn.cluster import AgglomerativeClustering
model = AgglomerativeClustering(linkage=linkage,
connectivity=connectivity, n_clusters=n_clusters)

#C降维算法
#主成分方法（PCA）
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
#核函主成分（kernal pca）
from sklearn.decomposition import KernelPCA
kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
#因子分析（Factor Analysis）
from sklearn.decomposition import FactorAnalysis
fa = FactorAnalysis()

#D文本挖掘算法
#主题生成模型（Latent Dirichlet Allocation）
#潜在语义分析（latent semantic analysis）
from sklearn.decomposition import NMF, LatentDirichletAllocation

#E分类算法
#线性判别分析（LDA）
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#二次判别分析（QDA）
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
#支持向量机回归（SVR）
from sklearn import svm
clf = svm.SVR()
#导入支持向量算法
from sklearn.svm import SVC
#KNN算法
from sklearn.neighbors import KNeighborsClassifier
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
#神经网络
from sklearn.neural_network import MLPClassifier
#决策树算法
from sklearn import tree
#贝叶斯算法
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB 
from sklearn.naive_bayes import BernoulliNB 

#F集成算法（Ensemble methods）
#Bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
bagging = BaggingClassifier(KNeighborsClassifier(),
                             max_samples=0.5, max_features=0.5)
#随机森林
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10)
#AdaBoost
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=100)
#GBDT（Gradient Tree Boosting）
from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
max_depth=1, random_state=0).fit(X_train, y_train)

