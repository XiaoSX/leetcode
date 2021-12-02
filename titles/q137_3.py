#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-31
'''
import random
class Solution:
    def singleNumber(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            k = random.randint(left, right)
            nums[right], nums[k] = nums[k], nums[right]
            low, high = left, right - 1
            while low <= high:
                while low < right and nums[low] <= nums[right]:
                    low += 1
                while high >= left and nums[high] > nums[right]:
                    high -= 1
                if low < high:
                    nums[low], nums[high] = nums[high], nums[low]
                    low += 1
                    high -= 1
            nums[right], nums[low] = nums[low], nums[right]
            pre_half = low - left + 1
            if pre_half % 3 == 1:
                right = low
            else:
                left = low + 1
        return nums[left]



