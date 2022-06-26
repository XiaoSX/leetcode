#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/7
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        max_ans = 0
        for t in s:
            if t == '(':
                ans += 1
            elif t == ')':
                ans -= 1
            else:
                pass
            max_ans = max(max_ans, ans)
        return max_ans