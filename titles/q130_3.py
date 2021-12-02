#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-18
'''

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def is_visit(cur_i, cur_j):
            return cur_i >= 0 and cur_i < m and cur_j >= 0 and cur_j < n and \
                   visit[cur_i][cur_j] == 0 and board[cur_i][cur_j] == 'O'

        def is_board(cur_i, cur_j):
            return cur_i == 0 or cur_i == m - 1 or cur_j == 0 or cur_j == n - 1

        total_graph = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visit[i][j] == 0:
                    cur_i, cur_j = i, j
                    graphs = [(cur_i, cur_j)]
                    visit[cur_i][cur_j] = 1
                    flag = True
                    queues = [(cur_i, cur_j)]
                    while len(queues) > 0:
                        cur_i, cur_j = queues.pop(-1)
                        if flag and is_board(cur_i, cur_j):
                            flag = False

                        for p in range(4):
                            ni, nj = cur_i + dirs[p][0], cur_j + dirs[p][1]
                            if is_visit(ni, nj):
                                visit[ni][nj] = 1
                                graphs.append((ni, nj))
                                queues.append((ni, nj))

                    total_graph += 1
                    if flag:
                        for pi, pj in graphs:
                            board[pi][pj] = 'X'