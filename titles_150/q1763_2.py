#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/6
'''

class Solution:

    def longestNiceSubstring(self, s: str) -> str:
        if s == '':
            return ''

        final_ans = ''
        lower, upper = 0, 0
        for i in range(len(s)):
            if s[i].islower():
                lower |= 1 << (ord(s[i]) - ord('a'))
            else:
                upper |= 1 << (ord(s[i]) - ord('A'))
        if lower == upper:
            return s

        init_i = 0
        valid = lower & upper
        for i in range(len(s)):
            if valid & (1 << (ord(s[i].lower()) - ord('a'))) == 0:
                ans = self.longestNiceSubstring(s[init_i: i])
                init_i = i + 1
                if len(final_ans) < len(ans):
                    final_ans = ans
        ans = self.longestNiceSubstring(s[init_i:])
        if len(final_ans) < len(ans):
            final_ans = ans
        return final_ans
