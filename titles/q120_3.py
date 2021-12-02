#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

class Solution:
    def search(self, triangle, i, j, f):
        if i == len(triangle):
            return 0

        if f[i][j] == '#':
            f[i][j] = triangle[i][j] + min(self.search(triangle, i + 1, j, f), self.search(triangle, i + 1, j + 1, f))
        return f[i][j]

    def minimumTotal(self, triangle) -> int:
        f = [['#' for _ in x] for x in triangle]
        return self.search(triangle, 0, 0, f)