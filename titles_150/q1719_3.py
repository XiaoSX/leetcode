#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/18
'''

from typing import  List
from collections import defaultdict


# links 数
# adj 结合的特征, 祖先关系, 或者存在多种关系, 或者不存在可行关系
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for edge in pairs:
            x, y = edge
            adj[x].add(y)
            adj[y].add(x)

        root = next((node for node in adj if len(adj[node]) == len(adj) - 1 ), -1)
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue

            currDegree = len(neighbours)
            parent = -1
            parentDegree = float('inf')
            for neighbour in neighbours:
                if currDegree <= len(adj[neighbour]) < parentDegree:
                    parent = neighbour
                    parentDegree = len(adj[neighbour])
            if parent == -1 or any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours):
                return 0

            if currDegree == parentDegree:
                ans = 2
        return ans