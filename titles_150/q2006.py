#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/9
'''

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        max_v = 100
        shift = max_v
        bound = shift + 2 * max_v
        dp = [[0 for _ in range(bound)] for _ in range(3)]
        # 初始偏移100
        dp[0][shift] = 1

        for x in nums:
            for i in range(2, 0, -1):
                for j in range(-shift, 2 * max_v):
                    dp[i][j+shift] = dp[i][j+shift]
                    if i == 1:
                        if j == x:
                            dp[i][j + shift] += 1
                        continue

                    if 0 <= x - j + shift < bound:
                        dp[i][j + shift] += dp[i - 1][x - j + shift]
                    if 0 <= x + j + shift < bound:
                        dp[i][j + shift] += dp[i - 1][x + j + shift]


        return dp[2][k+shift]