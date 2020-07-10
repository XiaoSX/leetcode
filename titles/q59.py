#  -*-  coding: utf-8  -*-
from math import ceil
class Solution:
    def generateMatrix(self, n: int):
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = [i for i in range(1, n * n + 1)]

        round = ceil(n / 2.0)

        i = 0
        j = 0
        ni = 0
        ans[i][j] = num[ni]
        ni += 1
        for p in range(round):
            while j + 1 < n - p:
                j += 1
                ans[i][j] = num[ni]
                ni += 1

            if i + 1 == n - p:
                break

            while i + 1 < n - p:
                i += 1
                ans[i][j] = num[ni]
                ni += 1

            if j == p:
                break

            while j - 1 >= p:
                j -= 1
                ans[i][j] = num[ni]
                ni += 1

            while i - 1 > p:
                i -= 1
                ans[i][j] = num[ni]
                ni += 1
        return ans

