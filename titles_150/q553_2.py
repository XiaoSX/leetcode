#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/27
'''

from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return '{}/{}'.format(nums[0], nums[1])
        return '{}/({})'.format(nums[0], '/'.join([str(cur) for cur in nums[1:]]))
