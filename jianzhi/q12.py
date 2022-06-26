#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/28
'''

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def search(p, w):
            if w == '':
                return True

            x, y = p
            if board[x][y] == w[0]:
                visit[x][y] = 1
                if w[1:] == '':
                    return True

                for d in direction:
                    dx, dy = d
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                        if search((nx, ny), w[1:]):
                            return True
                visit[x][y] = 0
            return False

        for i in range(m):
            for j in range(n):
                if search((i, j), word):
                    return True
        return False