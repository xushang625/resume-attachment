# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:03:16 2022
写一个决策树桩，也就是单层决策树（只有一个根节点和两个叶子节点）。要点如下：
1.只考虑二分类问题，类别标签为0和1。
2.Class名称为Stump。包含三个方法，即__init__，fit和predict。其中__init__方法无需添加代码。
3.在fit方法中，需要计算出用来进行划分的特征编号(self.ifeature)和划分阈值(self.thres)。
4.predict方法需要预测出与输入X行数等长的预测值。
@author: 31479
"""

import numpy as np

class Stump:
    
    def __init__(self):
        # 这里没有什么需要做的
        pass
        
    def fit(self, X, Y):
        # 把拟合过程写在这里
        # 要正确选择用来分割的特征和划分阈值
        # 假设都是连续特征        
        gini_index = [0,0]
        best = [0,0]
        for A in range(2):
            a = sorted(X[:,A])
            T = []
            gini = []
            for i in range(len(X)-1):
                T.append((a[i] + a[i+1]) / 2)
            for t in T:
                x1, x2, y1 ,y2 = [], [], [], []
                for i in range(len(X)):
                    if(X[i][A]<t):
                        x1.append(1)
                        if(Y[i]==1):
                            y1.append(1)
                    if(X[i][A]>t):
                        x2.append(2)
                        if(Y[i]==1):
                            y2.append(1)
                gini1 = 1-(len(y1)/len(x1))**2
                gini2 = 1-(len(y2)/len(x2))**2
                gini.append((len(x1)/len(X))*gini1 + (len(x2)/len(X))*gini2)
            gini_index[A] = min(gini)
            best[A] = T[gini.index(min(gini))]
        self.thres = best[gini_index.index(min(gini_index))]
        self.ifeature = gini_index.index(min(gini_index))
    
    def predict(self, X):
        pred = np.zeros(shape = len(X))
        for i in range(len(X)):
            if(X[i][self.ifeature]>self.thres):
                pred[i] = 1
            else:
                pred[i] = 0
        return pred