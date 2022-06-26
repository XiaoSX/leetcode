#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-04
'''


# 难点在于，剩余和补给会互相转化，最优子结构不好写
import numpy as np
class Solution:
    def cut_state(self, states):
        N = len(states)

        for i in range(N - 1):
            if states[i] is None:
                continue
            m, p = states[i]
            for j in range(i+1, N):
                if states[j] is None:
                    continue
                n, q = states[j]
                if p == q:
                    if m <= n:
                        states[j] = None
                        continue
                    else:
                        states[i] = None
                        break
                elif p < q:
                    if m - p <= n - q:
                        states[j] = None
                    continue
                else:
                    if n - q <= m - p:
                        states[i] = None
                        break
                    else:
                        continue

        return [x for x in states if x is not None]


    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        if m == 0:
            return 0
        if not isinstance(dungeon[0], list):
            dungeon = np.array(dungeon).reshape(1, -1)

        m = len(dungeon)
        n = len(dungeon[0])
        f = [[[] for _ in range(n)] for _ in range(m)]  # states
        if dungeon[0][0] <= 0:
            f[0][0].append([1 - dungeon[0][0], 1])
        else:
            f[0][0].append([0, dungeon[0][0]])

        j = 0
        for i in range(1, n):
            cur = dungeon[j][i]
            f[j][i].append([f[j][i - 1][0][0], f[j][i - 1][0][1] + cur])
            if f[j][i][0][1] <= 0:
                f[j][i][0][0] += 1 - f[j][i][0][1]
                f[j][i][0][1] = 1

        i = 0
        for j in range(1, m):
            cur = dungeon[j][i]
            f[j][i].append([f[j - 1][i][0][0], f[j - 1][i][0][1] + cur])
            if f[j][i][0][1] <= 0:
                f[j][i][0][0] += 1 - f[j][i][0][1]
                f[j][i][0][1] = 1

        for i in range(1, m):
            for j in range(1, n):
                cur = dungeon[i][j]
                for state in f[i][j - 1] + f[i - 1][j]:
                    need, left = state
                    n_left = left + cur
                    n_need = need
                    if n_left <= 0:
                        n_need += 1 - n_left
                        n_left = 1
                    f[i][j].append([n_need, n_left])
                f[i][j] = self.cut_state(f[i][j])


        return max(min([x[0] for x in f[m - 1][n - 1]]), 1)