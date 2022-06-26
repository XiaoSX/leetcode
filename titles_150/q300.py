#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/15
'''

from typing import List
import numpy as np

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        location = [-1 for _ in range(n)]
        for i in range(1, n):
            max_v = float('-inf')
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    if nums[j] >= max_v:
                        max_v = nums[j]
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            location[i] = j

        ith = np.argmax(dp)
        ans = []
        while 1:
            ans.append(nums[ith])
            ith = location[ith]
            if ith == -1:
                break
        print(ans[::-1])
        return max(dp)
