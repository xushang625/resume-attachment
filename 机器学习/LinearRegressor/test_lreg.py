# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:42:33 2022

@author: 31479
"""

from lreg import LinearRegressor
import unittest
import numpy as np
class TestLreg(unittest.TestCase):
    def test_fit(self):
        # 构造输入矩阵，20个样本，2个变量
        X = np.random.normal(size=(20, 2))
        # 人为指定2个变量对应的系数
        beta_real = np.array([10, 2]).reshape((-1, 1))
        # 指定截距值
        intercept_real = 10
        # 根据系数和截距构造样本输出值，并对输出值添加随机干扰
        Y = X @ beta_real + intercept_real + np.random.normal(scale=0.001, size=(20, 1))
        # 新建模型
        model = LinearRegressor()
        # 拟合模型
        model.fit(X, Y)
        # 预测，仍旧使用X来进行预测
        pred = model.predict(X)
        # 检查模型拟合的系数shape是否符合要求
        self.assertEqual(model.beta.shape, (3, 1))
        # 检查截距项是否正确，在10上下浮动0.5以内
        self.assertAlmostEqual(model.beta[0], 10, delta = 0.5)
        # 检查模型预测的结果shape是否符合要求
        self.assertEqual(pred.shape, (20, 1))
        # 检查拟合的r2值是否正常，这里检查是否大于0.9
        r2 = 1 - np.mean((pred - Y)**2) / np.var(Y)
        self.assertGreater(r2, 0.9)
unittest.main()