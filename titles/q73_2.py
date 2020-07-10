#  -*-  coding: utf-8  -*-
# 问题的关键在于用访问过的元素做标记
# 标记元素最后更新
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_column = False

        for i in range(m):
            for j in range(n):
                if j == 0:
                    if matrix[i][j] == 0:
                        zero_column = True
                        matrix[i][0] = 0
                else:
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if zero_column:
            for i in range(m):
                matrix[i][0] = 0

