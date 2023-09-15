# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:11:06 2022

@author: 31479
"""

import numpy as np

class LogisticRegressionClassifier:
    def sigmoid(self,a: np.ndarray):
        return 1 / (1 + np.exp(-a))
    
    def __init__(self):
        self.beta = None
        
    def fit(self, X, Y):
        # 输入的Y是样本类别，值为0或者1
        # 把模型系数放在beta属性中，其中第0个元素是截距
        # 也就是说，如果X有3列，则beta的尺寸是(4, 1)
        X = np.insert(X, 0, 1, axis = 1)
        eta = 0.05
        self.beta = np.zeros((4, 1))
        for _ in range(1000):
            for xnow, ynow in zip(X, Y):
                xnow = xnow.reshape((-1, 1))
                # 这一行就是随机梯度下降法的更新公式
                self.beta = self.beta + eta * (ynow - self.sigmoid(self.beta.T @ xnow)) * xnow
    
    def predict(self, X):
        # predict方法预测正类（也就是类别1）的概率
        X = np.insert(X, 0, 1, axis = 1)
        pred = self.sigmoid(X @ self.beta)
        return pred
    
    