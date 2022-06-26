#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/9
'''

class Solution:
    # dp[x][y] 到目前为止（顺序）, 和是x的y个数，有几种可能
    # 当前阶段的dp，依赖于上阶段dp值，所以必须是倒序，否则前面的值会被更新为当前阶段
    def countQuadruplets(self, nums) -> int:
        dp = [[0 for _ in range(4)] for _ in range(101)]
        dp[0][0] = 1
        ans = 0
        for i in range(len(nums)):
            t = nums[i]
            # 到当前为止，和最小是当前值
            for x in range(100, t-1, -1):
                for y in range(3, 0, -1):
                    dp[x][y] += dp[x - t][y - 1]

            ans += dp[t][3]
        return ans
