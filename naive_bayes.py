# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:16:52 2018

决策树和Naïve Bayes，前者的建模过程是逐步递进，每次拆分只有一个变量参与，
这种建模机制含有抗多重共线性干扰的功能；后者干脆假定变量之间是相互独立的，
因此从表面上看，也没有多重共线性的问题。但是对于回归算法，不论是一般回归，逻辑回归，
或存活分析，都要同时考虑多个预测因子，因此多重共线性是不可避免的。
"""
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

trees=10000
cancer=load_breast_cancer()
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,random_state=0)

multinomialNB=MultinomialNB()
bernoulliNB=BernoulliNB()
gaussianNB=GaussianNB()
multinomialNB.fit(x_train,y_train)
bernoulliNB.fit(x_train,y_train)
gaussianNB.fit(x_train,y_train)

print("MultinomialNB:")  
print("accuracy on the training subset:{:.3f}".format(multinomialNB.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(multinomialNB.score(x_test,y_test)))

print("bernoulliNB:")  
print("accuracy on the training subset:{:.3f}".format(bernoulliNB.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(bernoulliNB.score(x_test,y_test)))

print("gaussianNB:")  
print("accuracy on the training subset:{:.3f}".format(gaussianNB.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(gaussianNB.score(x_test,y_test)))
'''
MultinomialNB:
accuracy on the training subset:0.894
accuracy on the test subset:0.902
bernoulliNB:
accuracy on the training subset:0.627
accuracy on the test subset:0.629
gaussianNB:
accuracy on the training subset:0.951
accuracy on the test subset:0.937
'''