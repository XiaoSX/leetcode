#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/28
'''

class Solution:
    def numWays(self, n: int) -> int:
        k = 1000000007
        f0 = 1
        f1 = 1
        for i in range(2, n + 1):
            f2 = (f0 + f1) % k
            f0 = f1
            f1 = f2
        return f1
