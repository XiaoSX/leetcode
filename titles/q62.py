#  -*-  coding: utf-8  -*-
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            d[m - 1][i] = 1

        for i in range(m):
            d[i][n - 1] = 1

        i = m - 2
        while i >= 0:
            j = n - 2
            while j >= 0:
                d[i][j] = d[i + 1][j] + d[i][j + 1]
                j -= 1
            i -= 1

        return d[0][0]