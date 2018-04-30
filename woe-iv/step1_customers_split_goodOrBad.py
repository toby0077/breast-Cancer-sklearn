# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:45:43 2018

@author  QQ：231469242

把数据源分类为两个Excel，好客户Excel数据和坏客户Excel数据
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#读取文件
readFileName="breast_cancer_总.xlsx"

#保存文件
saveFileName_good="result_good.xlsx"
saveFileName_bad="result_bad.xlsx"

#读取excel
df=pd.read_excel(readFileName)
#帅选数据
df_good=df[df.diagnosis=="B"]
df_bad=df[df.diagnosis=="M"]

#保存数据
df_good.to_excel(saveFileName_good, sheet_name='Sheet1')
df_bad.to_excel(saveFileName_bad, sheet_name='Sheet1')


