# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:23:01 2022

@author: 31479
"""

import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

#csv文件导入
#训练集
train_data = pd.read_csv('df_train.csv')
x_train = train_data.iloc[:,+1:].values
y_train = train_data.iloc[:,:1].values
#测试集
test_data = pd.read_csv('df_test_without_Y.csv')
x_test = test_data.iloc[:,1:].values

#数据标准化
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#训练模型
clf = GradientBoostingRegressor()
rf = clf.fit (x_train, y_train.ravel())

#预测结果
pred = clf.predict(x_test)

#数据输出到csv文件
data1 = test_data.iloc[:,0]
data2 = pd.DataFrame({'Ypred':pred})
dataframe = pd.concat([data1,data2],axis=1)
dataframe.to_csv('df_pred_20202733.csv',index=False,sep=',')