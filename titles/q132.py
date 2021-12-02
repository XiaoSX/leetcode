#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-11
'''

class Solution:
    def minCut(self, s: str) -> int:
        new_s = '#'.join(s)
        n = len(s)
        dis = [[0 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
        for i in range(2 * n - 1):
            dis[i][i] = 1

        for l in range(2, 2 * n - 1, 2):
            for i in range(2 * n - 1 - l):
                if dis[i + 1][i + l - 1] == 1 and new_s[i] == new_s[i + l]:
                    dis[i][i + l] = 1

        new_dis = [[dis[i][j] for j in range(0, 2 * n - 1, 2)] for i in range(0, 2 * n - 1, 2)]
        visit = [0 for _ in range(n)]
        queues = [-1, '#']
        step = 0
        while len(queues) > 0:
            start_p = queues.pop(0)
            if start_p == '#':
                step += 1
                queues.append('#')
                continue
            for i in range(start_p + 1, n):
                if visit[i] == 0 and new_dis[start_p + 1][i] == 1:
                    if i == n - 1:
                        return step
                    queues.append(i)
                    visit[i] = 1
