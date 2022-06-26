#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/31
'''

class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        low = 0
        high = low
        while high < n:
            while high < n and nums[low] == nums[high]:
                high += 1
            if high >= n:
                break
            nums[low] = None
            nums[high] = None
            high += 1
            while low < n and nums[low] is None:
                low += 1
        if low < n:
            return nums[low]
        else:
            return -1