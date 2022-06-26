#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/10
'''

from typing import List

def factor(m, n):
    if m == n:
        return m

    if m < n:
        m, n = n, m
    return factor(m - n, n)

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                if factor(i, j) > 1:
                    continue
                else:
                    ans.append(str(j) + '/' + str(i))
                    if i -j != j:
                        ans.append(str(i-j) + '/' + str(i))
        return ans
