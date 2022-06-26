#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-03
'''

class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums = sorted(nums)
        max_v = 0
        for i in range(n-1):
            max_v = max(max_v, nums[i+1] - nums[i])
        return max_v
