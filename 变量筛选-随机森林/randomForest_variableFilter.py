# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 09:30:24 2018

@author: Administrator
随机森林不需要预处理数据
"""
import pandas as pd
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
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
forest=RandomForestClassifier(n_estimators=trees,random_state=0)
forest.fit(x_train,y_train)

print("random forest with %d trees:"%trees)  
print("accuracy on the training subset:{:.3f}".format(forest.score(x_train,y_train)))
print("accuracy on the test subset:{:.3f}".format(forest.score(x_test,y_test)))
print('Feature importances:{}'.format(forest.feature_importances_))


n_features=data.shape[1]
plt.barh(range(n_features),forest.feature_importances_,align='center')
plt.yticks(np.arange(n_features),feature_names)
plt.title("random forest with %d trees:"%trees)
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.show()


'''
accuracy on the training subset:1.000
accuracy on the test subset:0.958
'''