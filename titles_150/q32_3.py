#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/21
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        for i in range(n):
            if s[i] == ')':
                if i > 0 and s[i - 1] == '(':
                    dp[i + 1] = dp[i - 1] + 2
                elif i > 0 and s[i - 1] == ')' and i - dp[i] - 1 >=0 and s[i - dp[i] - 1] == '(':
                    dp[i + 1] = dp[i - dp[i] - 1] + dp[i] + 2
        return max(dp)