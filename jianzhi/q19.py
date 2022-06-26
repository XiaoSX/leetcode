#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/25
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m+1):
            for i in range(n+1):

                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if i > 0 and not dp[i][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if i > 0 and (p[j - 1] == s[i - 1] or p[j - 1] == '.'):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[n][m]