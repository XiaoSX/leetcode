#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/11
'''

from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # SIZE = 1000000
        SIZE = 6
        visit = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        q = [source]
        visit[source[0]][source[1]] = 1
        blocked_set = set()
        for b in blocked:
            blocked_set.add((b[0], b[1]))
        while len(q) > 0:
            node = q.pop(0)
            x, y = node
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if nx < SIZE and ny < SIZE and nx >= 0 and ny >= 0 and visit[nx][ny] == 0 and \
                        (nx, ny) not in blocked_set:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])
                    if nx == target[0] and ny == target[1]:
                        return True
        return False
