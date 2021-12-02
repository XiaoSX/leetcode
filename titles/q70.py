# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 下午5:03
# @Author  : RenMeng
# @File    : q70.py

class Solution:
    def climbStairs(self, n: int) -> int:
        # f[i] = f[i - 1] + f[i - 2]
        # 考虑n<2 的边界
        if n == 0:
            return 0
        f = [0 for _ in range(n + 1)]
        f[1] = 1
        if n == 1:
            return f[n]
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]