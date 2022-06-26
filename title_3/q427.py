#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/29
'''

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from typing import List
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        amount = sum(map(sum, grid))
        if amount == n * n or amount == 0:
            node = Node(val=int(amount > 0), isLeaf=True, topLeft=None, topRight=None,
                        bottomLeft=None, bottomRight=None)
            return node
        else:
            node = Node(val=1, isLeaf=False, topLeft=None, topRight=None,
                        bottomLeft=None, bottomRight=None)
            node.topLeft = self.construct(grid[:n // 2, :n//2])
            node.topRight = self.construct(grid[:n // 2, n//2:])
            node.bottomLeft = self.construct(grid[n // 2:, :n//2])
            node.bottomRight = self.construct(grid[n // 2:, n//2:])
            return node