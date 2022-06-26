#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-02
'''

class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            elif nums[low] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] < nums[mid]:
                high = mid - 1
            else:
                high = mid
        return nums[low]
