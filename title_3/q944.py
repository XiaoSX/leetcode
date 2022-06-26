#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/12
'''

from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        if m == 0:
            return m

        n = len(strs[0])
        cnt = 0
        for i in range(n):
            p = strs[0][i]
            for j in range(1, m):
                q = strs[j][i]
                if q < p:
                    cnt += 1
                    break
                p = q
        return cnt
