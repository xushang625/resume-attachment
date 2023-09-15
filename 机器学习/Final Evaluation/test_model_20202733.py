# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:45:19 2022

@author: 31479
"""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('df_train.csv')
x = dataset.iloc[:,1:].values
y = dataset.iloc[:,:1].values

#分割训练集和测试集，这里没有写random_state是因为准备多次测试不同模型的分数
x_train ,x_test ,y_train ,y_test = train_test_split(x, y, test_size=0.3)

#数据标准化
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#下面为对各种回归模型性能的简单测试，多次随机分割后会发现GradientBoostingRegressor的score总是最高的
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
rf = clf.fit (x_train, y_train.ravel())
print("LinearRegression结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.neighbors import KNeighborsRegressor
clf = KNeighborsRegressor()
rf = clf.fit (x_train, y_train.ravel())
print("KNeighborsRegressor结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.svm import SVR
clf = SVR()
rf = clf.fit (x_train, y_train.ravel())
print("SVR结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.tree import DecisionTreeRegressor
clf = DecisionTreeRegressor()
rf = clf.fit (x_train, y_train.ravel())
print("DecisionTreeRegressor结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.linear_model import Ridge
clf = Ridge()
rf = clf.fit (x_train, y_train.ravel())
print("Ridge结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.linear_model import Lasso
clf = Lasso()
rf = clf.fit (x_train, y_train.ravel())
print("Lasso结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.ensemble import RandomForestRegressor
clf = RandomForestRegressor()
rf = clf.fit (x_train, y_train.ravel())
print("RandomForestRegressor结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.ensemble import AdaBoostRegressor
clf = AdaBoostRegressor()
rf = clf.fit (x_train, y_train.ravel())
print("AdaBoostRegressor结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.ensemble import GradientBoostingRegressor
clf = GradientBoostingRegressor()
rf = clf.fit (x_train, y_train.ravel())
print("GradientBoostingRegressor结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))

from sklearn.ensemble import BaggingRegressor
clf = BaggingRegressor()
rf = clf.fit (x_train, y_train.ravel())
print("BaggingRegressor结果如下：")
print("训练集分数：",rf.score(x_train,y_train))
print("验证集分数：",rf.score(x_test,y_test))
