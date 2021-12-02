#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-18
'''

class UnionFind:
    # 并查集的三种基本操作: 合并联通；找其父节点；节点间是否联通
    def __init__(self, totalNodes):
        self.parents = {}
        for i in range(totalNodes):
            self.parents[i] = i

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parents[root2] = root1

    def find(self, node):
        while self.parents[node] != node:
            node = self.parents[self.parents[node]]
        return node

    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)

class Solution:
    # 并查集
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        #用一个虚拟节点, 边界上的O的父节点都是这个虚拟节点
        uf = UnionFind(rows * cols + 1)
        dummyNode = rows * cols

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        uf.union(i * cols + j, dummyNode)
                    else:
                        if i > 0 and board[i - 1][j] == 'O':
                            uf.union(i * cols + j, (i - 1) * cols + j)
                        if j > 0 and board[i][j - 1] == 'O':
                            uf.union(i * cols + j, i * cols + j - 1)
                        if i < rows - 1 and board[i + 1][j] == 'O':
                            uf.union(i * cols + j, (i + 1) * cols + j)
                        if j < cols - 1 and board[i][j + 1] == 'O':
                            uf.union(i * cols + j, i * cols + j + 1)

        for i in range(rows):
            for j in range(cols):
                if uf.isConnected(i * cols + j, dummyNode):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        debug = {}
        for i in range(rows):
            for j in range(cols):
                debug[(i, j)] = uf.find(i * cols + j)
        print(debug)
        print(uf.find(24))
