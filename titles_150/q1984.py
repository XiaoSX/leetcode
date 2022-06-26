#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/11
'''

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        min_v = nums[-1] - nums[0]
        for i in range(len(nums) - k + 1):
            tmp = nums[i + k - 1] - nums[i]
            if tmp < min_v:
                min_v = tmp

        return min_v
