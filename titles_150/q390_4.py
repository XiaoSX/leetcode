#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/2
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        begin = 1
        step = 1
        l_2_r = True
        while n > 1:
            if l_2_r | n & 1 == 1:
                begin += step

            step <<= 1
            n >>= 1
            l_2_r = not l_2_r

        return begin