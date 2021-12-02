#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

class Solution:
    def minimumTotal(self, triangle) -> int:
        f = list(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                f[j] = min(f[j], f[j + 1]) + triangle[i][j]

        return f[0]