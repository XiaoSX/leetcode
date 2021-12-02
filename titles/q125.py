#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-27
'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if re.search('^[a-zA-Z0-9]$', s[i]) is None:
                i += 1
                continue
            if re.search('^[a-zA-Z0-9]$', s[j]) is None:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

