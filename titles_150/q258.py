#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/3
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            cur = 0
            while num:
                a = num % 10
                num = num // 10
                cur += a
            num = cur
        return num
