#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a