# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:31:54 2022

@author: 31479
"""

import numpy as np

class LinearRegressor:
    
    def __init__(self):
        self.beta = None
        
    def fit(self, X, Y):
        X = np.insert(X, 0, 1, axis = 1)
        self.beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
    
    def predict(self, X):
        X = np.insert(X, 0, 1, axis = 1)
        pred = X.dot(self.beta)
        return pred