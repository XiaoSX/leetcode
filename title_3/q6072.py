#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/17
'''

from typing import List
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp_row = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        dp_col = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                cur = grid[i - 1][j - 1]
                while cur % 10 == 0:
                    dp_row[i][j][2] += 1
                    dp_col[i][j][2] += 1
                    cur = cur % 10
                while cur % 2 == 0:
                    cur = cur // 2
                    dp_row[i][j][0] += 1
                    dp_col[i][j][0] += 1
                while cur % 5 == 0:
                    cur = cur // 5
                    dp_row[i][j][1] += 1
                    dp_col[i][j][1] += 1

                for k in range(3):
                    dp_row[i][j][k] += dp_row[i][j - 1][k]
                    dp_col[i][j][k] += dp_col[i - 1][j][k]

                dp_row[i][j][2] += min(dp_row[i][j][0], dp_row[i][j][1])
                dp_row[i][j][1] -= min(dp_row[i][j][0], dp_row[i][j][1])
                dp_row[i][j][0] -= min(dp_row[i][j][0], dp_row[i][j][1])

                dp_col[i][j][2] += min(dp_col[i][j][0], dp_col[i][j][1])
                dp_col[i][j][1] -= min(dp_col[i][j][0], dp_col[i][j][1])
                dp_col[i][j][0] -= min(dp_col[i][j][0], dp_col[i][j][1])


        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if cur % 10 == 0 or cur % 5 == 0:
                    for k in range(4):
                        pass
