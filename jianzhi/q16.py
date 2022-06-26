#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/24
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        sign = -1 if n < 0 else 1
        n = abs(n)

        while n >= 1:
            if n % 2 == 1:
                ans *= x
                n = n - 1
            else:
                n = n // 2
                x *= x
        if sign == -1:
            ans = 1 / ans
        return ans