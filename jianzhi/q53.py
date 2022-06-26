#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/28
'''

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if mid < nums[mid]:
                high = mid
            else:
                low = mid + 1

        if low < n:
            return nums[low] - 1
        else:
            return nums[-1] + 1