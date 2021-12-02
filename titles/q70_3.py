# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午4:59
# @Author  : RenMeng
# @File    : q70_3.py

# 数列的通项公式
# f1 = 1, f2 = 2, f2是数列的第三项
# (f0=0, f1=1, f2=1, 斐波那契数列)
import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        return int((np.power((1 + np.sqrt(5)) / 2, n + 1) - np.power((1 - np.sqrt(5)) / 2, n + 1)) / np.sqrt(5))