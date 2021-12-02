#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-10
'''

class Solution:
    def longestConsecutive(self, nums) -> int:
        a = {}
        for i in nums:
            a[i] = i
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] - 1 not in a:
                cur = nums[i]
                while cur + 1 in a:
                    cur += 1
                ans = max(ans, cur- nums[i] + 1)
        return ans