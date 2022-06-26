#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-18
'''
from functools import cmp_to_key
class Solution:
    def compare(self, a, b):
        if a + b > b + a:
            return 1
        elif a + b < b + a:
            return -1
        else:
            return 0

    def largestNumber(self, nums) -> str:
        nums = [str(x) for x in nums]
        nums.sort(cmp=self.compare, reverse=True)
        # nums = sorted(nums, key=cmp_to_key(self.compare), reverse=True)
        return ''.join(nums) if nums[0] != '0' else '0'