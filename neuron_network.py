# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 11:49:50 2018

@author: Administrator
神经网络需要预处理数据
"""
#Multi-layer Perceptron 多层感知机
from sklearn.neural_network import MLPClassifier
#标准化数据，否则神经网络结果不准确，和SVM类似
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import mglearn
import matplotlib.pyplot as plt
import numpy as np


mglearn.plots.plot_logistic_regression_graph()
mglearn.plots.plot_single_hidden_layer_graph()

cancer=load_breast_cancer()
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=42)

mlp=MLPClassifier(random_state=42)
mlp.fit(x_train,y_train)
print("neural network:")    
print("accuracy on the training subset:{:.3f}".format(mlp.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(mlp.score(x_test,y_test)))

scaler=StandardScaler()
x_train_scaled=scaler.fit(x_train).transform(x_train)
x_test_scaled=scaler.fit(x_test).transform(x_test)

mlp_scaled=MLPClassifier(max_iter=1000,random_state=42)
mlp_scaled.fit(x_train_scaled,y_train)
print("neural network after scaled:")    
print("accuracy on the training subset:{:.3f}".format(mlp_scaled.score(x_train_scaled,y_train)))
print("accuracy on the test subset:{:.3f}".format(mlp_scaled.score(x_test_scaled,y_test)))


mlp_scaled2=MLPClassifier(max_iter=1000,alpha=1,random_state=42)
mlp_scaled2.fit(x_train_scaled,y_train)
print("neural network after scaled and alpha change to 1:")    
print("accuracy on the training subset:{:.3f}".format(mlp_scaled2.score(x_train_scaled,y_train)))
print("accuracy on the test subset:{:.3f}".format(mlp_scaled2.score(x_test_scaled,y_test)))


#绘制颜色图,热图
plt.figure(figsize=(20,5))
plt.imshow(mlp_scaled.coefs_[0],interpolation="None",cmap="GnBu")
plt.yticks(range(30),cancer.feature_names)
plt.xlabel("columns in weight matrix")
plt.ylabel("input feature")
plt.colorbar()



