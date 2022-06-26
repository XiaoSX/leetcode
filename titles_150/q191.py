#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/20
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            n &= (n - 1)
            cnt += 1
        return cnt