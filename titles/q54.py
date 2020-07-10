#  -*-  coding: utf-8  -*-
from math import ceil
class Solution:
    def spiralOrder(self, matrix):
        ans = []
        m = len(matrix)
        if m == 0:
            return ans
        if type(matrix[0]) == list:
            n = len(matrix[0])
        else:
            return matrix

        count = ceil(min(m, n) / 2.0)

        i = 0
        j = 0
        ans.append(matrix[i][j])
        for p in range(count):
            while j < n - p - 1:
                j += 1
                ans.append(matrix[i][j])

            if i == m - p - 1:
                break

            while i < m - p - 1:
                i += 1
                ans.append(matrix[i][j])


            if j == p:
                break

            while j >= p + 1:
                j -= 1
                ans.append(matrix[i][j])

            while i > p + 1:
                i -= 1
                ans.append(matrix[i][j])
        return ans

