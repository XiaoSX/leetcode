#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/21
'''

from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:

        graph = {}
        n = len(arr)
        visit = [0 for _ in range(n)]
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        queues = [0]
        visit[0] = 1
        cnt = 0
        while len(queues) > 0:
            q_size = len(queues)
            for i in range(q_size):
                ni = queues[i]
                if ni == n - 1:
                    return cnt

                if ni + 1 < n and visit[ni + 1] == 0:
                    queues.append(ni + 1)
                    visit[ni + 1] = 1
                if ni - 1 >= 0 and visit[ni - 1] == 0:
                    queues.append(ni - 1)
                    visit[ni - 1] = 1
                for j in graph[arr[ni]]:
                    if visit[j] == 0:
                        queues.append(j)
                        visit[j] = 1
                        # list 在动态遍历的时候不能remove其元素
                        # graph[arr[ni]].remove(j)
                graph[arr[ni]] = []
            cnt += 1
            queues = queues[q_size:]

