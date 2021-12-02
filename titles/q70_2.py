# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 上午11:09
# @Author  : RenMeng
# @File    : q70_2.py

# 矩阵的快速幂运算
import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        factor = np.array([[1, 1], [1, 0]])
        res = np.eye(2)
        while n != 0:
            if n % 2 != 0:
               res = np.dot(res, factor)
               n -= 1
            else:
                factor = np.dot(factor, factor)
                n = n // 2
        # ans = np.dot(res, np.array([1, 0]).reshape(2, 1))
        return int(res[0][0])