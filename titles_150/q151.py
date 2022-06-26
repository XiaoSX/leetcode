#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-03
'''

import re
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        ns = list(s)
        j = n
        i = j - 1
        while i >= 0:
            if re.search('^[a-zA-Z0-9]$', ns[i]):
                ns[j - 1] = ns[i]
                j -= 1
                i -= 1
            elif ns[i] == ' ' and j < n and ns[j] != ' ':
                ns[j - 1] = ns[i]
                i -= 1
                j -= 1
            else:
                i -= 1
        real_n = n - j
        # 末尾的空格不要
        if ns[j] == ' ':
            real_n -= 1
        # 指针移动之后剩余的元素无效，要clear
        while j > 0:
            ns[j - 1] = ' '
            j -= 1
        i = 0
        j = 0
        while i < n:
            if ns[i] != ' ':
                j = i
                while i < n and ns[i] != ' ':
                    i += 1
                p = i - 1
                while j < p:
                    ns[j], ns[p] = ns[p], ns[j]
                    j += 1
                    p -= 1
            else:
                i += 1
        i = 0
        j = n - 1
        while i < j:
            ns[i], ns[j] = ns[j], ns[i]
            i += 1
            j -= 1
        return ''.join(ns[:real_n])


