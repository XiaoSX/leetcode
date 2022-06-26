#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/28
'''

from typing import List




class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        graph = [[0 for _ in range(n)] for _ in range(n)]
        for edge in requests:
            x, y = edge
            graph[x][y] += 1

        visit = [0 for _ in range(n)]
        seen = [0 for _ in range(n)]
        paths = []
        circle_paths = set()

        def dfs(node):
            if visit[node] == 1:
                ni = paths.index(node)
                circle_paths.add(tuple(sorted(paths[ni:])))
                return

            visit[node] = 1
            seen[node] = 1
            paths.append(node)
            for j in range(n):
                if graph[node][j] > 0:
                    dfs(j)
            paths.pop(-1)
            visit[node] = 0

        for i in range(n):
            if seen[i] == 0:
                dfs(i)

        max_v = 0
        edge_graph = {}
        for circle in circle_paths:
            pn = len(circle)
            for i in range(pn):
                if i == pn - 1:
                    j = 0
                else:
                    j = i + 1
                edge = tuple(sorted([circle[i], circle[j]]))
                if edge not in edge_graph:
                    edge_graph[edge] = set()
                edge_graph[edge].add(circle)

        for edge in edge_graph:
            max_cnt = 0
            circles = edge_graph[edge]
            for pnodes in circles:
                cnt = float('inf')
                pn = len(pnodes)
                for i in range(pn):
                    if i == pn - 1:
                        j = 0
                    else:
                        j = i + 1
                    cnt = min(graph[pnodes[i]][pnodes[j]], cnt)
                cnt *= pn
                max_cnt = max(max_cnt, cnt)
            max_v += max_cnt
        return max_v