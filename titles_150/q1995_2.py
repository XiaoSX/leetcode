#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/3
'''

class Solution:
    # dp[x][y] 到目前为止（顺序）， 和是x的y个数，有几种可能
    # 当前值的和，一定是基于之前值（dp已经生成，因为是顺利遍历nums）
    def countQuadruplets(self, nums) -> int:
        dp = [[0 for _ in range(4)] for _ in range(101)]
        dp[0][0] = 1
        ans = 0
        for x in nums:
            ans += dp[x][3]
            # 所以bixu倒序遍历,不然就不是之前值，而是现阶段值，
            for i in range(100, x - 1, -1):
                for j in range(3, 0, -1):
                    dp[i][j] += dp[i - x][j - 1]
        return ans