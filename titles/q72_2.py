#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-04
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, n):
            ans[0][i] = i
        for i in range(1, m):
            ans[i][0] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1]
                else:
                    ans[i][j] = min(ans[i - 1][j], ans[i][j - 1], ans[i - 1][j - 1]) + 1

        return ans[m - 1][n - 1]