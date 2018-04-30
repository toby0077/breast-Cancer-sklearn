# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 22:13:30 2018

@author: QQ:231469242
woe负数，好客户<坏客户
woe正数，好客户>坏客户
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#创建save文件
newFile=os.mkdir("save/") 

#读取文件
FileName_good="result_good.xlsx"
FileName_bad="result_bad.xlsx"

#保存文件
saveFileName="result_woe_iv.xlsx"

#读取excel
df_good=pd.read_excel(FileName_good)
df_bad=pd.read_excel(FileName_bad)

#所有变量列表
list_columns=list(df_good.columns[:-1])

index=0

def Ratio_goodDevideBad(index):
    #第一列字段名（好客户属性）
    columnName=list(df_good.columns)[index]

    #第一列好客户内容和第二列坏客户内容
    column_goodCustomers=df_good[columnName]
    column_badCustomers=df_bad[columnName]

    #去掉NAN
    num_goodCustomers=column_goodCustomers.dropna()
    #统计数量
    num_goodCustomers=num_goodCustomers.size

    #去掉NAN
    num_badCustomers=column_badCustomers.dropna()
    #统计数量
    num_badCustomers=num_badCustomers.size
    

    #第一列频率分析
    frenquency_goodCustomers=column_goodCustomers.value_counts()
    #第二列频率分析
    frenquency_badCustomers=column_badCustomers.value_counts()
   
    #各个元素占比
    ratio_goodCustomers=frenquency_goodCustomers/num_goodCustomers
    ratio_badCustomers=frenquency_badCustomers/num_badCustomers
    #最终好坏比例
    ratio_goodDevideBad=ratio_goodCustomers/ratio_badCustomers
    return (columnName,num_goodCustomers,num_badCustomers,frenquency_goodCustomers,frenquency_badCustomers,ratio_goodCustomers,ratio_badCustomers,ratio_goodDevideBad)

#woe函数,阵列计算
def Woe(ratio_goodDevideBad):
    woe=np.log(ratio_goodDevideBad)
    return woe

'''    
#iv函数,阵列计算
def Iv(woe):
    iv=(ratio_goodCustomers-ratio_badCustomers)*woe
    return iv
    '''

#iv参数评估,参数iv_sum（变量iv总值）
def Iv_estimate(iv_sum):
    #如果iv值大于0.02，为有效因子
    if iv_sum>0.02:
        print("informative")
        return "A"
    #评估能力一般
    else:
        print("not informative")
        return "B"
   
    
'''
#详细参数输出
def Print():
    print ("columnName:",columnName)
    Iv_estimate(iv_sum)
    print("iv_sum",iv_sum)
    #print("",)
    #print("",)
    '''
    
#详细参数保存到excel，save文件里    
def Write_singleVariable_to_Excel(index):
    #index为变量索引，第一个变量，index=0
    ratio=Ratio_goodDevideBad(index)
    columnName,num_goodCustomers,num_badCustomers,frenquency_goodCustomers,frenquency_badCustomers,ratio_goodCustomers,ratio_badCustomers,ratio_goodDevideBad=ratio[0],ratio[1],ratio[2],ratio[3],ratio[4],ratio[5],ratio[6],ratio[7]

    woe=Woe(ratio_goodDevideBad)
    iv=(ratio_goodCustomers-ratio_badCustomers)*woe
    
    df_woe_iv=pd.DataFrame({"num_goodCustomers":num_goodCustomers,"num_badCustomers":num_badCustomers,"frenquency_goodCustomers":frenquency_goodCustomers,
    "frenquency_badCustomers":frenquency_badCustomers,"ratio_goodCustomers":ratio_goodCustomers,
    "ratio_badCustomers":ratio_badCustomers,"ratio_goodDevideBad":ratio_goodDevideBad,
    "woe":woe,"iv":iv},columns=["num_goodCustomers","num_badCustomers","frenquency_goodCustomers","frenquency_badCustomers",
    "ratio_goodCustomers","ratio_badCustomers","ratio_goodDevideBad","woe","iv"])
    
    
    #sort_values(by=...)用于对指定字段排序
    df_sort=df_woe_iv.sort_values(by='iv',ascending=False)

    #ratio_badDevideGood数据写入到result_compare_badDevideGood.xlsx文件
    df_sort.to_excel("save/"+columnName+".xlsx")


    #计算iv总和，评估整体变量
    iv_sum=sum([i for i in iv if np.isnan(i)!=True])

    print ("变量:",columnName)
    #iv参数评估,参数iv_sum（变量iv总值）
    iv_estimate=Iv_estimate(iv_sum)
    print("iv_sum",iv_sum)
    return iv_estimate,columnName



#y\有价值变量列表存储器
list_Informative_variables=[]


#写入所有变量参数,保存到excel里，save文件
for i in range(len(list_columns)):
    status=Write_singleVariable_to_Excel(i)[0]
    columnName=Write_singleVariable_to_Excel(i)[1]
    
    if status=="A":
        list_Informative_variables.append(columnName)

        

