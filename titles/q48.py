#  -*-  coding: utf-8  -*-

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return matrix
        b_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp = matrix[i][j]
                f_i = n - 1 - j
                f_j = i
                while b_matrix[f_i][f_j] == 1:
                    _t = f_j
                    f_j = f_i
                    f_i = n - 1 - _t
                matrix[i][j] = matrix[f_i][f_j]
                matrix[f_i][f_j] = tmp
                b_matrix[i][j] = 1


