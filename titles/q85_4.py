# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 上午11:14
# @Author  : RenMeng
# @File    : q85_4.py

class Solution:
    # area = 以当前点为右下结束点的height=k的面积
    def maximalRectangle(self, matrix) -> int:
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                for k in range(i + 1):
                    if matrix[i - k][j] == '0':
                        break
                    if j == 0:
                        heights[i][j][k] = k + 1
                    else:
                        heights[i][j][k] = heights[i][j - 1][k] + k + 1
                    max_area = max(max_area, heights[i][j][k])
        return max_area