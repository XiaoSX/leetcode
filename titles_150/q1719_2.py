#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/16
'''

from typing import List
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        degree = {}
        for edge in pairs:
            x, y = edge
            if x not in degree:
                degree[x] = set()
            degree[x].add(y)

            if y not in degree:
                degree[y] = set()
            degree[y].add(x)

        found_root = 0
        all_nodes = len(degree)
        many_trees = False

        for node in degree:
            cur_d = len(degree[node])
            if cur_d == all_nodes - 1:
                found_root += 1

            for nj in degree[node]:
                degree[node].remove(nj)
                degree[nj].remove(node)

                if len(degree[node]) > len(degree[nj]):
                    inter_d = degree[node].intersection(degree[nj])
                    if inter_d != degree[nj]:
                        return 0
                elif len(degree[node]) < len(degree[nj]):
                    inter_d = degree[node].intersection(degree[nj])
                    if inter_d != degree[node]:
                        return 0
                else:
                    if degree[node] != degree[nj]:
                        return 0
                    many_trees = True

                degree[node].add(nj)
                degree[nj].add(node)

        if found_root >= 1:
            return 2 if many_trees else 1
        return 0


