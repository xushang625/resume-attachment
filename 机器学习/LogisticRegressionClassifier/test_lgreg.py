# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:15:04 2022

@author: 31479
"""

from lgreg import LogisticRegressionClassifier
import unittest
import numpy as np
class Testlgreg(unittest.TestCase):
    def sigmoid(a: np.ndarray):
        return 1 / (1 + np.exp(-a))
    def test_fit(self):
        # 这个方法测试逻辑回归模型fit方法能否正确估计参数
        # --------------------------------------------------------------
        # 这里的代码块模拟训练样本
        n_samp = 1000
        # 模拟的样本有3个特征，下面是真实的系数和截距
        beta_real = np.random.uniform(low=-10, high=10, size=(3, 1))
        intercept_real = np.random.uniform(low=-10, high=10, size=1)
        X = np.random.normal(size=(n_samp, 3))
        # 这里计算模拟样本出现正类的真实概率
        prob_posi = Testlgreg.sigmoid(X @ beta_real + intercept_real)
        def sim_y_label(prob_posi):
            # 这里根据轮盘赌算法，根据正类的概率模拟样本的类别
            a = np.random.uniform(low=0, high=1, size=1)
            if a < prob_posi:
                return 1
            else:
                return 0
        # 将上面的函数向量化
        v_sim_y_label = np.vectorize(sim_y_label)
        # 模拟每个样本的类别
        Y = v_sim_y_label(prob_posi)
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # 拟合模型并预测正类的概率
        model = LogisticRegressionClassifier()
        model.fit(X, Y)
        prob_pred = model.predict(X)
        # --------------------------------------------------------------
        # 检查模型拟合的系数shape是否符合要求
        self.assertEqual(model.beta.shape, (4, 1))
        # 检查截距项是否正确，在真实值上下浮动2以内
        self.assertAlmostEqual(model.beta[0], intercept_real, delta = 2)
        # 检查每个系数是否正确，在真实值上下浮动2以内
        self.assertAlmostEqual(model.beta[1], beta_real[0], delta = 2)
        self.assertAlmostEqual(model.beta[2], beta_real[1], delta = 2)
        self.assertAlmostEqual(model.beta[3], beta_real[2], delta = 2)
        # 检查模型预测的结果shape是否符合要求
        self.assertEqual(prob_pred.shape, (n_samp, 1))
        # 检查预测概率范围
        self.assertLessEqual(np.max(prob_pred), 1)
unittest.main()