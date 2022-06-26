#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/16
'''

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, i, res = len(nums), 0, 0
        for j in range(n):
            if j == 0 or nums[j] != nums[j - 1]:
                while i < n and (nums[i] < nums[j] + k or i <= j):
                    i += 1
                if i < n and nums[i] == nums[j] + k:
                    res += 1
        return res
