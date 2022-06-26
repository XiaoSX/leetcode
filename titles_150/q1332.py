#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/22
'''

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n - 1
        while i < j and i < n and j > 0 and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return 1
        return 2