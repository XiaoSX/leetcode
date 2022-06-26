#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/22
'''

class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == 0:
            return 0


        sign = 1
        if (a > 0 and b < 0) or (a <0 and b > 0):
            sign = -1

        a = abs(a)
        b = abs(b)

        ans = 0
        old_b = b
        cnt = 1
        while a >= b:
            if b + b <= a:
                b += b
                cnt *= 2
                if b == a:
                    ans += cnt
                    break
            else:
                a -= b
                b = old_b
                ans += cnt
                cnt = 1

        if sign == 1:
            if ans >= (1 << 31):
                ans = (1 << 31) - 1
            return ans
        else:
            if ans >= (1 << 31):
                ans = (1 << 31)
        return ans * sign
