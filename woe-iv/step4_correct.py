# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:26:34 2018

@author: QQ:231469242
过滤样本量少于5的iv值
把save文档数据分类保存到good_ivResult，medium_ivResult，low_ivResult，goodOrSuspicious_ivResult四个文件夹里
最终生成一个包含有价值的变量的excel
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#创建四个文件,存放不同变量
file_good=os.mkdir("good_ivResult") 
file_medium=os.mkdir("medium_ivResult") 
file_low=os.mkdir("low_ivResult") 
file_goodOrSuspicious=os.mkdir("goodOrSuspicious_ivResult") 


#读取save文件的excel
#所有excel文件  
file_List=os.listdir("NewSave/") 

#对单个文件分类
def Classify_singleExcel(filename):
    print("文件名：",filename)
    df=pd.read_excel("save/"+filename)
    #columnName=df.columns

    #df数据转换为阵列
    values=df.values
    #跑完叠加单个变量所有的子变量iv总数
    iv_sum=0
    for i in values:
        #如果好客户或坏客户频率数小于5，就无实际参考价值，其iv值记为0分。
        if i[2]>5 and i[3]>5:
            #print("True")
            #print("num1:",i[2])
            #print("num2:",i[3])
            #print("iv:",i[8])
            iv_sum+=i[8]


    #iv值高，存入file_good文件夹
    if 0.5>iv_sum>0.3:
        print("good informative")
        print("iv_sum",iv_sum)
        df.to_excel("good_ivResult/"+filename, sheet_name='Sheet1')
        #dict_goodInformative_variables[]=iv_sum

    #评估能力一般，存入file_medium文件夹
    if 0.3>iv_sum>0.1:
        print("medium informative")
        print("iv_sum",iv_sum)
        df.to_excel("medium_ivResult/"+filename, sheet_name='Sheet1')

    #评估能力差，存入file_low文件夹
    if 0.1>iv_sum>=0:
        print("low informative") 
        print("iv_sum",iv_sum)
        df.to_excel("low_ivResult/"+filename, sheet_name='Sheet1')  
    
    
    #评估能力强或可疑,存入file_goodOrSuspicious文件夹
    if iv_sum>0.5:
        print("goodOrSuspicious informative")
        print("iv_sum",iv_sum)
        df.to_excel("goodOrSuspicious_ivResult/"+filename, sheet_name='Sheet1')      
    
#对所有文件分类    
def Classify_allExcels():   
    for fileName in file_List:
        Classify_singleExcel(fileName)

#对所有文件分类 
Classify_allExcels()


#获取有价值变量，然后建模
valueable_variable_List=os.listdir("good_ivResult/")+os.listdir("medium_ivResult/")+os.listdir("goodOrSuspicious_ivResult/") 
valueable_variable_List=[i.strip(".xlsx") for i in valueable_variable_List] 


#读取文件
readFileName="breast_cancer_总.xlsx"

#最终表格，存储有价值变量
df_all_valueableVariable=pd.DataFrame()
#读取excel
df=pd.read_excel(readFileName)

for i in valueable_variable_List:
    df_one_valuableVariable=df[i]
    #横向连接两个变量字段
    df_all_valueableVariable=pd.concat([df_all_valueableVariable,df_one_valuableVariable],axis=1)

df_all_valueableVariable.to_excel("标签规则_有效因子.xlsx")

