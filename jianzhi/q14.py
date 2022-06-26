#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/24
'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        ans = 1
        for m in range(2, n):

            k = n // m

            if k == 0:
                continue
            b = n % m
            a = m - b
            _ans = 1
            while b > 0:
                _ans *= (k + 1)
                b -= 1

            while a > 0:
                _ans *= k
                a -= 1


            ans = max(ans, _ans)

        ans %= 1000000007
        return ans
