#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/25
'''

class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1:
            cnt += n // 2
            n = n // 2 + (1 if n % 2 != 0 else 0)
        return cnt