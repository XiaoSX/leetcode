#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-13
'''
import math
class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        min_v = min(nums)
        max_v = max(nums)
        d = max((max_v - min_v) // (n - 1), 1)
        buckets = {}
        for cur in nums:
            cur_d = (cur - min_v) // d
            if cur_d not in buckets:
                buckets[cur_d] = [float('inf'), float('-inf')]
            buckets[cur_d][0] = min(buckets[cur_d][0], cur)
            buckets[cur_d][1] = max(buckets[cur_d][1], cur)
        pri_max = None
        max_margin = 0
        for i in range(n):
            if i in buckets:
                if pri_max:
                    max_margin = max(max_margin, buckets[i][0] - pri_max)
                pri_max = buckets[i][1]
        return max_margin