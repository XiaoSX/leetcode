#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/17
'''

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                      (1, -2), (-1, -2), (1, 2), (-1, 2)]

        dp = [[[1.0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        for s in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    p = 0
                    for d in directions:
                        ni = i + d[0]
                        nj = j + d[1]
                        if 0 <= ni < n and 0 <= nj < n:
                            p += 1.0 / 8 * dp[s-1][ni][nj]
                    dp[s][i][j] = p
                    if s == k and i == row and j == column:
                        return dp[s][i][j]
        return dp[k][row][column]


