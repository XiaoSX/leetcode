#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/24
'''

class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        if n == 0:
            return 0
        f = 1
        for i in range(2, n+1):
            _tmp = f + f0
            f0 = f
            f = _tmp
            f %= 1000000007
            # f %= 3
            # print(i, f)
        return f