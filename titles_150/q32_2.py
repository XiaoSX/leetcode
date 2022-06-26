#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/21
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        n = len(s)
        max_v = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack[-1] >= 0 and s[stack[-1]] == '(':
                    stack.pop(-1)
                    max_v = max(max_v, i - stack[-1])

                else:
                    max_v = max(max_v, i - stack[-1] - 1)
                    stack.append(i)

        max_v = max(max_v, n - stack[-1] - 1)
        return max_v