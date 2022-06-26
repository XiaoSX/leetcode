#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/8
'''

from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        ans = []
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            else:
                ans.append(nums)
        return ans