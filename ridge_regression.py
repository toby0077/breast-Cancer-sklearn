# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:46:25 2018

@author: Administrator
"""
from sklearn.kernel_ridge import KernelRidge
from sklearn import linear_model
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer


cancer=load_breast_cancer()
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,random_state=0)
#岭回归
reg=linear_model.Ridge (alpha = .5)
reg.fit(x_train,y_train)

print("Ridge regression:")  
print("accuracy on the training subset:{:.3f}".format(reg.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(reg.score(x_test,y_test)))


#核岭回归（Kernel ridge regression）
#kernelRidge=KernelRidge(kernel='rbf', alpha=0.1, gamma=10)
kernelRidge=KernelRidge(kernel='rbf')
kernelRidge.fit(x_train,y_train)
print("KernelRidge:")  
print("accuracy on the training subset:{:.3f}".format(kernelRidge.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(kernelRidge.score(x_test,y_test)))
'''
Ridge regression:
accuracy on the training subset:0.757
accuracy on the test subset:0.722
KernelRidge:
accuracy on the training subset:0.360
accuracy on the test subset:-1.593
'''