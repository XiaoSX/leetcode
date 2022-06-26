#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/25
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans = ''
        for i in range(len(words) - 1, -1, -1):
            if words[i] == '':
                continue
            ans += words[i]
            ans += ' '
        return ans[:-1]