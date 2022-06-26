#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/4
'''
DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def __init__(self):
        self.n = 0
        self.dp = None

    def getResult(self, graph, mouse, cat, turn):
        if turn >= 2 * self.n:
            return DRAW
        if mouse == 0:
            return MOUSE_WIN
        if mouse == cat:
            return CAT_WIN

        res = self.dp[mouse][cat][turn]
        if res != -1:
            return res

        next_move = mouse if turn % 2 == 0 else cat
        default_res = MOUSE_WIN if next_move != mouse else CAT_WIN
        res = default_res     # 败局
        for node in graph[next_move]:
            next_mouse = node if next_move == mouse else mouse
            next_cat = cat if next_move == mouse else node
            if next_move == cat and node == 0:
                continue

            next_res = self.getResult(graph, next_mouse, next_cat, turn + 1)

            if next_res != default_res:
                res = next_res
                if next_res != DRAW:
                    break

        self.dp[mouse][cat][turn] = res
        return res


    def catMouseGame(self, graph) -> int:
        n = len(graph)
        self.n = len(graph)
        self.dp = [[[-1 for _ in range(2 * n)] for _ in range(n)] for _ in range(n)]
        return self.getResult(graph, 1, 2, 0)
