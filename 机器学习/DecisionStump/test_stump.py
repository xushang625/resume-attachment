# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:03:39 2022

@author: 31479
"""

import importlib
import numpy as np
from numpy.random import uniform
from numpy.random import randint
import stump
# 重新载入一下，确保能够更新你模块的修改
importlib.reload(stump)
# --------------------------------------------------------------
# 这里模拟训练样本
n_samp = 200
# 模拟样本有两个特征
X = uniform(low=0, high=10, size=(n_samp, 2))
# 随机选取一个特征来区分类别isel
isel = randint(low=0, high=2, size=1)[0]
# 随机选择一个分割阈值thres_set
thres_set = uniform(low=3, high=7, size=1)[0]
# 大于这个阈值为类别1
Y = np.zeros(shape=n_samp)
Y[X[:, isel] > thres_set] = 1
#import matplotlib.pyplot as plt
#plt.scatter(X[:, 0], X[:, 1], c=Y)
#plt.show()
# --------------------------------------------------------------
# import你的模块，拟合并预测两个样本
model = stump.Stump()
model.fit(X, Y)
pred1 = model.predict(np.array([[0, 0]]))
pred2 = model.predict(np.array([[10, 10]]))
# --------------------------------------------------------------
# 检查拟合的根节点的分割阈值是否正确
flag1 = np.abs(model.thres - thres_set) < 0.2
if not flag1:
    raise Exception('划分阈值不正确.')
# 检查模型预测的结果shape是否符合要求
flag2 = np.array_equal(pred1.shape, (1, )) | np.array_equal(pred1.shape, (1, 1))
flag3 = np.array_equal(pred2.shape, (1, )) | np.array_equal(pred2.shape, (1, 1))
if (not flag2) | (not flag3):
    raise Exception('预测结果形状不正确.')
# 检查预测类别是否正确
flag4 = pred1.reshape(-1)[0] == 0
flag5 = pred2.reshape(-1)[0] == 1
if (not flag4) | (not flag5):
    raise Exception('预测结果不正确.')
flag_final = flag1 & flag2 & flag3 & flag4 & flag5
if flag_final:
    print('通过所有测试!')