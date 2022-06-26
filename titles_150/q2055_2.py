#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/8
'''

from typing import  List
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pre_sum = [0 for _ in range(len(s))]
        right = [-1 for _ in range(len(s))]
        left = [-1 for _ in range(len(s))]
        cnt = 0
        l = -1
        for i in range(len(s)):
            if s[i] == '*':
                cnt += 1
            else:
                l = i

            pre_sum[i] = cnt
            left[i] = l

        r = -1
        for i in range(len(s) - 1, -1 , -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = []
        for q in queries:
            x, y = q
            x, y = right[x], left[y]
            if x < y and x >= 0 and y >= 0:
                ans.append(pre_sum[y] - pre_sum[x])
            else:
                ans.append(0)

        return ans
