#  -*-  coding: utf-8  -*-
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        skip_col = set()

        for i in range(m):
            zero_row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row = True
                    skip_col.add(j)
            if zero_row:
                for j in range(n):
                    matrix[i][j] = 0

        for j in skip_col:
            for i in range(m):
                matrix[i][j] = 0



