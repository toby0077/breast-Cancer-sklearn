# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:59:44 2018

@author: Toby，项目合作QQ：231469242
 radius半径
 texture结构，灰度值标准差
 symmetry对称

决策树找出强因子
worst radius
worst symmetry
worst texture
texture error

"""
import csv,pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydotplus 
from IPython.display import Image
import graphviz
from sklearn.tree import export_graphviz
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree 
from sklearn.model_selection import train_test_split
#交叉验证样本平均测试，评分更加
from sklearn.cross_validation import cross_val_score

#读取文件
readFileName="breast_cancer_变量筛选.xlsx"

#读取excel
df=pd.read_excel(readFileName)
# data为Excel前几列数据
data=df[df.columns[:-1]]
#标签为Excel最后一列数据
target=df[df.columns[-1:]]
#变量名
feature_names=list(df.columns[:-1])

x=data
y=target

featureNames=feature_names
#5.决策树
#建立决策树分类器
decisionTree= tree.DecisionTreeClassifier(max_depth=5)
decisionTree.fit(x,y) 
#交叉验证得分，返回数组
score_decisionTree=cross_val_score(decisionTree,x,y,cv=5,scoring='accuracy')
print("cross value decisionTree= score:",score_decisionTree.mean())






