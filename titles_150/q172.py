#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-09
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        base = 5
        num = n // base
        while num:
            ans += num
            base *= 5
            num = n // base
        return ans