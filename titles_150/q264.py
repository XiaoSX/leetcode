#!/usr/bin/qython
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/15
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        f2 = 1
        f3 = 1
        f5 = 1

        for i in range(2, n + 1):
            dp[i] = min(dp[f2] * 2, dp[f3] * 3, dp[f5] * 5)
            if dp[i] == dp[f2] * 2:
                f2 += 1
            if dp[i] == dp[f3] * 3:
                f3 += 1
            if dp[i] == dp[f5] * 5:
                f5 += 1

        return dp[n]
