# -*- coding: utf-8 -*-

'''
如果相邻数比较大，咋把0改为1

 #新加修改的语句，解决同盾分数[80,100]无数据问题    
        if math.isnan(value[2])==True and value[3]>500:
        if math.isnan(value[3])==True and value[2]>500:

'''

import os
import pandas as pd
import numpy as np
from pandas import Series
import math

#读取save文件的excel
#所有excel文件  
file_List=os.listdir("save/") 
newFile=os.mkdir("NewSave/") 


#修改单个excel数据，邻近数太大，此处无值，就设定为1
#测试Modify_single_excel("同盾分数段.xlsx")
def Modify_single_excel(excel):
    df=pd.read_excel("save/"+excel)
    #df数据转换为阵列
    values=df.values
    columns=df.columns
    index=df.index
    for i in range(len(values)):
        value=values[i]
         #邻近数太大，此处无值，就设定为1
        if math.isnan(value[2])==True and value[3]>500:
            #显示修改过的excel
            print("modified excel:",excel)
            value[2]=1
            #ratio_goodCustomers重新计算
            value[4]=value[2]/value[0]
            #ratio_goodDevideBad重新计算
            value[6]=value[4]/value[5]
            #woe重新计算
            value[7]=np.log(value[6])
            #iv重新计算
            value[8]=(value[4]-value[5])* value[7]
            
        if math.isnan(value[3])==True and value[2]>500:
            #显示修改过的excel
            print("modified excel:",excel)
            #frenquency_badCustomers设定为1
            value[3]=1
            #ratio_badCustomers重新计算
            value[5]=value[3]/value[1]
            #ratio_goodDevideBad重新计算
            value[6]=value[4]/value[5]
            #woe重新计算
            value[7]=np.log(value[6])
            #iv重新计算
            value[8]=(value[4]-value[5])* value[7]
    
    df_new=pd.DataFrame(data=values,columns=columns,index=index)
    df_new.to_excel("NewSave/"+excel)


#修改多个excel数据，邻近数太大，此处无值，就设定为1
def Modify_all_excels(file_List):

    for i in range(len(file_List)):
        excel=file_List[i]
        Modify_single_excel(excel)
        
        
Modify_all_excels(file_List)        
        
        