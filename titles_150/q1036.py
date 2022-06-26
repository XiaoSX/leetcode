#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/11
'''

from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        SIZE = 1000000
        visit = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        def DFS(sx, sy, tx, ty):
            if sx == tx and sy == ty:
                return True

            if sx >= SIZE or sx < 0:
                return False

            if sy >= SIZE or sy < 0:
                return False

            if visit[sx][sy] == 1:
                return False

            if [sx, sy] in blocked:
                return False


            direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            visit[sx][sy] = 1
            for d in direction:
                next_x = sx + d[0]
                next_y = sy + d[1]
                result = DFS(next_x, next_y, tx, ty)
                if result:
                    return True
            return False
        return DFS(source[0], source[1], target[0], target[1])