#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/25
'''

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        if m == 0:
            return ans

        n = len(matrix[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(min(m, n)):
            x = i
            y = i
            for d in direction:
                dx, dy = d
                while 1:
                    if 0 <= x < m and 0 <= y < n and visit[x][y] == 0:
                        ans.append(matrix[x][y])
                        visit[x][y] = 1

                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                        x = nx
                        y = ny
                    else:
                        break

        return ans



