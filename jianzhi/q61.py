#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/28
'''

from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        king = sum([1 for x in nums if x == 0])
        if king >= len(nums):
            return False
        pre = nums[king]
        i = king + 1
        while i < len(nums):
            if nums[i] > pre + 1:
                if king == 0:
                    return False
                king -= 1
                pre = pre + 1
            elif nums[i] == pre:
                return False
            else:
                pre = pre + 1
                i += 1
        return True