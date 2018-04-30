# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:04:14 2018

@author: Administrator
"""

from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
train_x, test_x, train_y, test_y=train_test_split(cancer.data,cancer.target,random_state=0)


import xgboost as xgb
dtrain=xgb.DMatrix(train_x,label=train_y)
dtest=xgb.DMatrix(test_x)

params={'booster':'gbtree',
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'max_depth':4,
    'lambda':10,
    'subsample':0.75,
    'colsample_bytree':0.75,
    'min_child_weight':2,
    'eta': 0.025,
    'seed':0,
    'nthread':8,
     'silent':1}

watchlist = [(dtrain,'train')]

bst=xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)

ypred=bst.predict(dtest)

# 设置阈值, 输出一些评价指标
y_pred = (ypred >= 0.5)*1

#模型校验
from sklearn import metrics
print ('AUC: %.4f' % metrics.roc_auc_score(test_y,ypred))
print ('ACC: %.4f' % metrics.accuracy_score(test_y,y_pred))
print ('Recall: %.4f' % metrics.recall_score(test_y,y_pred))
print ('F1-score: %.4f' %metrics.f1_score(test_y,y_pred))
print ('Precesion: %.4f' %metrics.precision_score(test_y,y_pred))
metrics.confusion_matrix(test_y,y_pred)

'''
模型区分能力相当好
AUC: 0.9981
ACC: 0.9860
Recall: 0.9889
F1-score: 0.9889
Precesion: 0.9889

'''



print("xgboost:")  
#print("accuracy on the training subset:{:.3f}".format(bst.get_score(train_x,train_y)))
#print("accuracy on the test subset:{:.3f}".format(bst.get_score(test_x,test_y)))
print('Feature importances:{}'.format(bst.get_fscore()))
'''
Feature importances:{'f20': 33, 'f27': 50, 'f21': 54, 'f1': 29, 'f7': 33, 'f22': 38, 
'f26': 17, 'f13': 46, 'f23': 41, 'f24': 13, 'f15': 2, 'f0': 6, 'f14': 5, 'f25': 7, 
'f3': 6, 'f12': 3, 'f9': 3, 'f28': 11, 'f8': 2, 'f10': 9, 'f6': 9, 'f16': 2, 'f29': 1, 
'f4': 4, 'f18': 3, 'f19': 2, 'f17': 2, 'f11': 1}
'''
'''
import matplotlib.pylab as plt
import pandas as pd
feat_imp = pd.Series(alg.booster().get_fscore()).sort_values(ascending=False)
feat_imp.plot(kind='bar', title='Feature Importances')
plt.ylabel('Feature Importance Score')
'''
#preds = bst.predict(test_x)


