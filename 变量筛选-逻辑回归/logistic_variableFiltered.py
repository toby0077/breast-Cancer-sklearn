# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:50:53 2018

@author: Administrator
"""
import pandas as pd
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

#读取文件
readFileName="breast_cancer_变量筛选.xlsx"
trees=10000

#读取excel
df=pd.read_excel(readFileName)
# data为Excel前几列数据
data=df[df.columns[:-1]]
#标签为Excel最后一列数据
target=df[df.columns[-1:]]
#变量名
feature_names=list(df.columns[:-1])

x_train,x_test,y_train,y_test=train_test_split(data,target,random_state=0)
#n_estimators表示树的个数，测试中100颗树足够
logist=LogisticRegression(C=1,penalty='l1',tol=0.0001)
#logist=LogisticRegression()
logist.fit(x_train,y_train)

print("logistic regression:")  
print("accuracy on the training subset:{:.3f}".format(logist.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(logist.score(x_test,y_test)))

'''
logistic regression:
accuracy on the training subset:0.986
accuracy on the test subset:0.944
'''

