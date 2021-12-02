#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

class Solution:
    def minimumTotal(self, triangle) -> int:
        f = [[float('inf') for _ in range(len(x) + 2)] for x in triangle]
        f[0][1] = triangle[0][0]
        for i in range(1, len(f)):
            for j in range(1, len(f[i]) - 1):
                f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j - 1]

        return min(*f[len(triangle) - 1])
