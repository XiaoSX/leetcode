#  -*-  coding: utf-8  -*-
class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        d = [[0 for _ in range(n)] for _ in range(m)]
        d[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(n-2, -1, -1):
            d[m - 1][i] = grid[m - 1][i] + d[m - 1][i + 1]
        for i in range(m-2, -1, -1):
            d[i][n - 1] = grid[i][n - 1] + d[i + 1][n - 1]

        i = m - 2
        while i >= 0:
            j = n - 2
            while j >= 0:
                d[i][j] = grid[i][j] + min(d[i + 1][j], d[i][j + 1])
                j -= 1
            i -= 1

        return d[0][0]
