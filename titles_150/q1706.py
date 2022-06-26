#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/24
'''

from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        def dfs(point):
            x, y = point
            if x == m:
                return y

            if grid[x][y] == 1:
                if y == n - 1 or grid[x][y + 1] != grid[x][y]:
                    return -1
                else:
                    return dfs((x+1, y+1))
            else:
                if y == 0 or grid[x][y - 1] != grid[x][y]:
                    return -1
                else:
                    return dfs((x+1, y-1))

        for i in range(n):
            ans.append(dfs((0, i)))
        return ans