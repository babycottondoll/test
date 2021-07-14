#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:51:53 2021

@author: wangchenxi
"""

'''
PPD拍拍贷风控预测
'''
import pandas as pd
import numpy as np

train=pd.read_csv('/Users/wangchenxi/Desktop/practice_python/PPD/PPD-First-Round-Data-Update/Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv',encoding='unicode_escape')
list(train.columns)

loginfo=pd.read_csv('/Users/wangchenxi/Desktop/practice_python/PPD/PPD-First-Round-Data-Update/Training Set/PPD_LogInfo_3_1_Training_Set.csv',encoding='unicode_escape')
loginfo.head()
loginfo.describe()

update=pd.read_csv('/Users/wangchenxi/Desktop/practice_python/PPD/PPD-First-Round-Data-Update/Training Set/PPD_Userupdate_Info_3_1_Training_Set.csv',encoding='unicode_escape')
