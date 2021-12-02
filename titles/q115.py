#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-24
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        if m == 0:
            return 0

        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(m + 1):
            f[0][i] = 0

        for i in range(n + 1):
            f[i][0] = 1

        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    f[i + 1][j + 1] = f[i][j] + f[i][j + 1]
                else:
                    f[i + 1][j + 1] = f[i][j + 1]

        return f[n][m]