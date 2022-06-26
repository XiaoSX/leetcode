#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/14
'''

from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if mid == low:
                return nums[mid]

            if nums[mid] == nums[mid - 1]:
                if (mid - low - 1) % 2 != 0:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (mid - low) % 2 != 0:
                    high = mid
                else:
                    low = mid
