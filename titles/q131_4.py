#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-29
'''
def dfs(start, end, graph, ans, total_ans, s):
    if start == end:
        total_ans.append(ans[:])
        return

    for j in range(start, len(graph)):
        if graph[start][j] == 1:
            ans.append(s[start:j+1])
            dfs(j + 1, end, graph, ans, total_ans, s)
            ans.pop(-1)




class Solution:
    def partition(self, s: str):
        ns = '#'.join(s)
        n = len(ns)
        # d[i][j]=1:s[i:(j+1)] huiwen
        d = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d[i][i] = 1

        for l in range(3, n + 1, 2):
            for i in range(0, n - l + 1):
                if d[i + 1][i + l - 2] and ns[i] == ns[i + l - 1]:
                    d[i][i + l - 1] = 1

        nd = [[d[i][j] for j in range(0, n, 2)] for i in range(0, n, 2)]
        ans = []
        total_ans = []
        dfs(0, len(s), nd, ans, total_ans, s)
        return total_ans
