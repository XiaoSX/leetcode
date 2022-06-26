#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/30
'''

from typing import List
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_v = max(nums)
        min_v = min(nums)
        if max_v - min_v <= k * 2:
            return 0
        return max_v - k - min_v - k