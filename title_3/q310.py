#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/6
'''

from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        min_height = 20000
        ans = []
        graph = [[] for _ in range(n)]
        for edge in edges:
            i_node, j_node  = edge
            graph[i_node].append(j_node)
            graph[j_node].append(i_node)


        for i in range(n):
            visit = [0 for _ in range(n)]
            queue = [i]
            visit[i] = 1
            cnt = 0
            while len(queue):
                q_size = len(queue)
                for ni in range(q_size):
                    node = queue[ni]
                    for j_node in graph[node]:
                        if visit[j_node] == 0:
                            visit[j_node] = 1
                            queue.append(j_node)
                queue = queue[q_size:]
                cnt += 1
            cnt -= 1
            if cnt < min_height:
                min_height = cnt
                ans = [i]
            elif cnt == min_height:
                ans.append(i)

        return ans