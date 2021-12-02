#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-14
'''


class Solution:
    def partition(self, s: str):
        n = len(s)
        f = [[True] * n for _ in range(n)]

        # 从后往前遍历
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret