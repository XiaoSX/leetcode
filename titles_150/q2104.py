#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/4
'''

from typing import List
import numpy as np

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        dp_min = [[float('inf') for _ in range(n)] for _ in range(n)]
        dp_max = [[float('-inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp_max[i][i] = nums[i]
            dp_min[i][i] = nums[i]

        ans = 0
        for i in range(1, n):
            for j in range(n-i):
                dp_min[j][j+i] = min(dp_min[j][j+i-1] , dp_min[j + 1][j+i])
                dp_max[j][j+i] = max(dp_max[j][j+i-1] , dp_max[j + 1][j+i])
                ans += dp_max[j][j+i] - dp_min[j][j+i]

        return ans



