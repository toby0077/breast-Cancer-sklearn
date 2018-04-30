# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:23:59 2018

@author: Administrator
QQ :231469242
统计score值，根据woe正负号确定取值。top+iv,top-iv
"""

import os
import pandas as pd
import numpy as np

#读取save文件的excel
#所有excel文件  
file_List=os.listdir("NewSave/") 

#score值词典
dict_score={}
#正负数分数字典
dict_positive_score={}
dict_negative_score={}
dict_zero_score={}

#读取单个excel变量的iv值，存入dict_score
def Singe_excel(excel):
    df=pd.read_excel("NewSave/"+excel)
    #df数据转换为阵列
    values=df.values
    index=df.index
    for i in range(len(values)):
        #print("i:",i)
        #excel的一行数据
        value=values[i]
        #woe符号确定分数正负号
        woe=value[7]
      
        #如果woe为正数，就取iv值
        if woe>0:  
           score=value[8]
        #如果woe为负数，取iv相反值
        if woe<0:
           score=-value[8]
        
        if woe==0:
           score=0
       
        #分变量名称，例如性别的男
        name=index[i]
        name=excel.strip(".xlsx")+"_"+str(name)
        
        #好坏客户频率数必须大于5，否则样本量过小，无统计学意义
        if value[2]>5 and value[3]>5:
            dict_score[name]=score
 
#读取所有excel变量的iv值，存入dict_iv
def All_excel(file_List):
    for i in range(len(file_List)):
        excel=file_List[i]  
        print(excel)
        Singe_excel(excel)            
            
#读取所有excel变量的iv值，存入dict_iv
All_excel(file_List)           

#把dict_score的子变量放入两个字典，分别存入正数因子，负数因子
for i in dict_score:
    #print(i)
    value=dict_score[i]  
    if value>0:
        dict_positive_score[i]=value            
    if value<0:
        dict_negative_score[i]=-value    
    if value==0:
        dict_zero_score[i]=value  
            

dict_positive_score_sorted=sorted(dict_positive_score.items(),key=lambda item:item[1],reverse=True)            
dict_negative_score_sorted=sorted(dict_negative_score.items(),key=lambda item:item[1],reverse=True)  

df_dict_positive_score_sorted=pd.DataFrame(data=dict_positive_score_sorted,columns=["子变量","分数"])
df_dict_positive_score_sorted.to_excel("标签规则_iv正分因子排名.xlsx")


df_dict_negative_score_sorted=pd.DataFrame(data=dict_negative_score_sorted,columns=["子变量","分数"])
df_dict_negative_score_sorted.to_excel("标签规则_iv负分因子排名.xlsx")
