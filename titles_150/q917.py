#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/23
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        n = len(ans)
        i = 0
        j = n - 1
        while i < j:
            if ans[i].isalpha() and ans[j].isalpha():
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
            elif not ans[i].isalpha():
                i += 1
            elif not ans[j].isalpha():
                j -= 1
            else:
                i += 1
                j -= 1

        return ''.join(ans)
