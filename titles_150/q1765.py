#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/29
'''

from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        ans = [[-1 for _ in range(n)]for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    ans[i][j] = 0

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(queue) > 0:
            q_size = len(queue)
            for i in range(q_size):
                x, y = queue[i]
                for d in direction:
                    nx = x + d[0]
                    ny = y + d[1]
                    if nx >= 0 and nx < m and ny >= 0 and ny < n:
                        if ans[nx][ny] == -1:
                            queue.append((nx, ny))
                            ans[nx][ny] = ans[x][y] + 1

                        # ans[nx][ny] = min(ans[nx][ny], ans[x][y] + 1)
            queue = queue[q_size:]

        return ans