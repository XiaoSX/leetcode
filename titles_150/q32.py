#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/21
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        split = [0 for _ in range(n)]
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if right > left:
                split[i] = 1
                left = 0
                right = 0

        left = 0
        right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left > right:
                split[i] = 1
                left = 0
                right = 0


        max_v = 0
        cnt = 0
        for i in range(n):
            if split[i] == 1:
                max_v = max(cnt, max_v)
                cnt = 0
                continue
            cnt += 1

        max_v = max(max_v, cnt)

        return max_v