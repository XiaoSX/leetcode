#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-18
'''

class Solution:
    def getConnectGraph(self, r, c, visit, board, graphs):
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        flag = True
        m = len(board)
        n = len(board[0])
        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
            flag = False
        for i in range(4):
            nr, nc = r + direction[i][0], c + direction[i][1]
            if nr < m and nc < n and nr >= 0 and nc >=0 and \
                board[nr][nc] == 'O' and visit[nr][nc] == 0:
                graphs.append((nr, nc))
                visit[nr][nc] = 1
                flag = flag & self.getConnectGraph(nr, nc, visit, board, graphs)
        return flag


    def replace(self, graph, board):
        for i, j in graph:
            board[i][j] = 'X'

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visit[i][j] == 0:
                    subgraph = [(i, j)]
                    visit[i][j] = 1
                    flag = self.getConnectGraph(i, j, visit, board, subgraph)
                    if flag:
                        self.replace(subgraph, board)