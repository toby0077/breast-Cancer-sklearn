# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 09:09:41 2018

@author:Toby 
standardScaler==features with a mean=0 and variance=1
minMaxScaler==features in a 0 to 1 range
normalizer==feature vector to a euclidean length=1

normalization
bring the values of each feature vector on a common scale
L1-least absolute deviations-sum of absolute values(on each row)=1;it is insensitive to outliers
L2-Least squares-sum of squares(on each row)=1;takes outliers in consideration during traing

"""

from sklearn import preprocessing
import numpy as np

data=np.array([[2.2,5.9,-1.8],[5.4,-3.2,-5.1],[-1.9,4.2,3.2]])
bindata=preprocessing.Binarizer(threshold=1.5).transform(data)
print('Binarized data:',bindata)

#mean removal
print('Mean(before)=',data.mean(axis=0))
print('standard deviation(before)=',data.std(axis=0))

#features with a mean=0 and variance=1
scaled_data=preprocessing.scale(data)
print('Mean(before)=',scaled_data.mean(axis=0))
print('standard deviation(before)=',scaled_data.std(axis=0))
print('scaled_data:',scaled_data)
'''
scaled_data: [[ 0.10040991  0.91127074 -0.16607709]
 [ 1.171449   -1.39221918 -1.1332319 ]
 [-1.27185891  0.48094844  1.29930899]]
'''

#features in a 0 to 1 range
minmax_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_minmax=minmax_scaler.fit_transform(data)
print('MinMaxScaler applied on the data:',data_minmax)
'''
MinMaxScaler applied on the data: [[ 0.56164384  1.          0.39759036]
 [ 1.          0.          0.        ]
 [ 0.          0.81318681  1.        ]]
'''

data_l1=preprocessing.normalize(data,norm='l1')
data_l2=preprocessing.normalize(data,norm='l2')
print('l1-normalized data:',data_l1)
'''
[[ 0.22222222  0.5959596  -0.18181818]
 [ 0.39416058 -0.23357664 -0.37226277]
 [-0.20430108  0.4516129   0.34408602]]
'''
print('l2-normalized data:',data_l2)
'''
[[ 0.3359268   0.90089461 -0.2748492 ]
 [ 0.6676851  -0.39566524 -0.63059148]
 [-0.33858465  0.74845029  0.57024784]]
'''



