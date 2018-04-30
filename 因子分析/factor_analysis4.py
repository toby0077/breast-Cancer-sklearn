# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 23:39:10 2018

@author: Administrator

scikit中的make_blobs方法常被用来生成聚类算法的测试数据，直观地说，make_blobs会根据
用户指定的特征数量、中心点数量、范围等来生成几类数据，这些数据可用于测试聚类算法的效果
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA

# X为样本特征，Y为样本簇类别， 共1000个样本，每个样本3个特征，共4个簇
X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2], 
                  random_state =9)
fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
plt.scatter(X[:, 0], X[:, 1], X[:, 2],marker='o')

'''
我们先不降维，只对数据进行投影，看看投影后的三个维度的方差分布.
可以看出投影后三个特征维度的方差比例大约为98.3%：0.8%：0.8%。投影后第一个特征占了绝大多数的主成分比例。
'''
pca = PCA(n_components=3)
pca.fit(X)
print (pca.explained_variance_ratio_)
print (pca.explained_variance_)

'''
现在我们来进行降维，从三维降到2维
'''
pca1 = PCA(n_components=2)
pca1.fit(X)
print (pca1.explained_variance_ratio_)
print (pca1.explained_variance_)

'''
可见降维后的数据依然可以很清楚的看到我们之前三维图中的4个簇
'''
X_new = pca1.transform(X)
plt.scatter(X_new[:, 0], X_new[:, 1],marker='o')
plt.show()

'''
现在我们看看不直接指定降维的维度，而指定降维后的主成分方差和比例
我们指定了主成分至少占95%，输出如下：

[ 0.98318212]
[ 3.78483785]
1

可见只有第一个投影特征被保留。这也很好理解，我们的第一个主成分占投影特征的方差比例高达98%。
只选择这一个特征维度便可以满足95%的阈值。
'''
pca2 = PCA(n_components=0.95)
pca2.fit(X)
print (pca2.explained_variance_ratio_)
print (pca2.explained_variance_)
print (pca2.n_components_)

'''
我们现在选择阈值99%看看
　此时的输出如下：

[ 0.98318212  0.00850037]
[ 3.78483785  0.03272285]
2
　　　　这个结果也很好理解，因为我们第一个主成分占了98.3%的方差比例，第二个主成分占了0.8%的方差比例，两者一起可以满足我们的阈值。
'''
pca3 = PCA(n_components=0.99)
pca3.fit(X)
print (pca3.explained_variance_ratio_)
print (pca3.explained_variance_)
print (pca3.n_components_)

'''
最后我们看看让MLE算法自己选择降维维度的效果
　输出结果如下：

[ 0.98318212]
[ 3.78483785]
1

　　　　可见由于我们的数据的第一个投影特征的方差占比高达98.3%，MLE算法只保留了我们的第一个特征。
'''
pca4 = PCA(n_components='mle')  
#pca4 = PCA()
pca4.fit(X)
print (pca4.explained_variance_ratio_)
print (pca4.explained_variance_)
print (pca4.n_components_)



