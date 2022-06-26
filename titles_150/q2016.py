#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/26
'''

from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_v = float('inf')
        max_v = 0
        ans = -1
        for cur in nums:
            if cur < min_v:
                if min_v < max_v:
                    ans = max(ans, max_v - min_v)
                min_v = cur
                max_v = cur
            elif cur > max_v:
                max_v = cur

        if min_v < max_v:
            ans = max(ans, max_v - min_v)
        return ans

# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans, premin = -1, nums[0]
#
#         for i in range(1, n):
#             if nums[i] > premin:
#                 ans = max(ans, nums[i] - premin)
#             else:
#                 premin = nums[i]
#
#         return ans
