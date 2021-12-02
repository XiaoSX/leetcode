#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-18
'''

class Solution:
    # dfs 非递归
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
                    graphs = []
                    flag = True
                    stacks = []
                    # 深度遍历, 如果可访问, 就访问其4个方向,不可访问, 就访问路上节点没有访问过的方向
                    while is_visit(cur_i, cur_j) or len(stacks) > 0:
                        if is_visit(cur_i, cur_j):
                            if flag and is_board(cur_i, cur_j):
                                flag = False
                            graphs.append((cur_i, cur_j))
                            visit[cur_i][cur_j] = 1
                            cur_dir = [0, 0, 0, 0]
                        else:
                            cur_i, cur_j, cur_dir = stacks.pop(-1)

                        for p in range(4):
                            if cur_dir[p] == 0:
                                ni, nj = cur_i + dirs[p][0], cur_j + dirs[p][1]
                                cur_dir[p] = 1
                                if is_visit(ni, nj):
                                    stacks.append((cur_i, cur_j, cur_dir))
                                    cur_i, cur_j = ni, nj
                                    break
                    total_graph += 1
                    if flag:
                        for pi, pj in graphs:
                            board[pi][pj] = 'X'
        # print(total_graph)