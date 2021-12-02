# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 下午3:28
# @Author  : RenMeng
# @File    : q96.py

class Solution:
    def numTrees(self, n: int) -> int:
        f = [0 for _ in range(n + 1)]
        if n == 0:
            return f[n]
        f[0] = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                f[i] += f[j - 1] * f[i - j]
        return f[n]
