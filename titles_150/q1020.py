#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/12
'''

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(point):
            x, y = point
            grid[x][y] = 0
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs((nx, ny))


        for i in [0, m-1]:
            for j in range(n):
                if grid[i][j] == 1:
                    dfs((i, j))

        for i in range(m):
            for j in [0, n-1]:
                if grid[i][j] == 1:
                    dfs((i, j))

        return sum([sum(x) for x in grid])