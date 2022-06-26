#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/17
'''

class Solution:
    def __init__(self):
        self.memory = {}

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                      (1, -2), (-1, -2), (1, 2), (-1, 2)]

        def dfs(p, step):
            cnt = 0

            x, y = p
            if x < 0 or x >= n or y < 0 or y >= n:
                return cnt

            if step == 0:
                return 1

            if (p, step) in self.memory:
                cnt += self.memory[(p, step)]
            else:
                for d in directions:
                    nx = x + d[0]
                    ny = y + d[1]
                    cnt += dfs((nx, ny), step-1)

            self.memory[(p, step)] = cnt
            return cnt

        cnt = dfs((row, column), k)
        total = pow(8, k)
        return cnt * 1.0 / total