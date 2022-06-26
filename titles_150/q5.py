#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/12
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(1, n):
            for j in range(n - i):
                if s[j] == s[j + i]:
                    if i <= 2:
                        dp[j][j + i] = 1
                    else:
                        dp[j][j + i] = dp[j + 1][j + i - 1]

        for i in range(n-1, -1, -1):
            for j in range(n - i):
                if dp[j][j + i] == 1:
                    return s[j:j+i+1]
