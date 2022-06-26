#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/20
'''

from typing import List
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        distance = [-1 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for e in edges:
            x, y = e
            graph[x].append(y)
            graph[y].append(x)

        queue = [0]
        d = -1
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                node = queue[i]
                distance[node] = d + 1

            for i in range(qsize):
                node = queue[i]
                for no in graph[node]:
                    if distance[no] == -1:
                        queue.append(no)
            d += 1

            queue = queue[qsize:]
        takes = [((distance[i] * 2 - 1) // patience[i] ) * patience[i] + distance[i] * 2 for i in range(1, n)]
        return max(takes) + 1