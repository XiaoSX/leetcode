#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-18
'''

class Solution:
    # dfs 非递归
    # 只要找边界上的O的联通子图就好了
    # 不需要subgraph集合, 不需要visit数组, 直接在当前board上做标志就好, 入栈也不需要方向数组, visit可表示已经访问过的方向
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
                    stacks = [(cur_i, cur_j)]
                    # 深度遍历, 如果可访问, 就访问其4个方向,不可访问, 就访问路上节点没有访问过的方向
                    # 深搜拿到栈顶元素就好了, 栈顶元素4个方向访问完就出栈
                    while len(stacks) > 0:
                        cur_i, cur_j = stacks[-1]
                        if flag and is_board(cur_i, cur_j):
                            flag = False

                        for p in range(4):
                            ni, nj = cur_i + dirs[p][0], cur_j + dirs[p][1]
                            if is_visit(ni, nj):
                                visit[ni][nj] = 1
                                graphs.append((ni, nj))
                                stacks.append((ni, nj))
                                break
                        else:
                            cur_i, cur_j = stacks.pop(-1)

                    total_graph += 1
                    if flag:
                        for pi, pj in graphs:
                            board[pi][pj] = 'X'
        print(total_graph)