#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/5
'''

from typing import List
class Solution:
    def __init__(self):
        self.max_value = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:



        def searchAllPath(node, value):
            node_t = nodeType(node)
            x, y = node
            cur_value = grid[x][y]
            if node_t == 0:
                self.max_value = max(self.max_value, value + cur_value)
                return

            x, y = node
            cur_value = grid[x][y]
            grid[x][y] = 0
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] != 0:
                    searchAllPath((nx, ny), value + cur_value)
            grid[x][y] = cur_value


        def nodeType(node):
            x, y = node
            cnt = 0
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] != 0:
                    cnt += 1

            return cnt


        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                node_t = nodeType((i, j))
                if node_t <= 2:
                    searchAllPath((i, j), 0)

        return self.max_value