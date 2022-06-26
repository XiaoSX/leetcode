#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-04
'''

class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        positive_max_v = [0 for _ in range(n)]
        negative_max_v = [0 for _ in range(n)]
        for i in range(n):
            positive_max_v[i] = max(nums[i], 0)
            negative_max_v[i] = min(nums[i], 0)
            if i == 0 or nums[i] == 0:
                continue
            positive_max_v[i] = max(positive_max_v[i - 1] * nums[i],
                                    nums[i],
                                    negative_max_v[i - 1] * nums[i])

            negative_max_v[i] = min(negative_max_v[i - 1] * nums[i],
                                    nums[i],
                                    positive_max_v[i - 1] * nums[i])
        return max(positive_max_v)