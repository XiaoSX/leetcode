# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 上午10:32
# @Author  : RenMeng
# @File    : q85_3.py

class Solution:
    # 底边长以及height延伸的最大宽度, 以每个点为边界的最大宽度
    def maximalRectangle(self, matrix) -> int:
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        widths = [[0 for _ in range(n)] for _ in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0:
                        widths[i][j] = 1
                    else:
                        widths[i][j] = widths[i][j - 1] + 1
        for i in range(m):
            for j in range(n):
                max_width = widths[i][j]
                max_area = max(max_area, max_width)
                for r in range(i - 1, -1, -1):
                    max_area = max(max_area, (i - r + 1) * min(max_width, widths[r][j]))
                    max_width = min(max_width, widths[r][j])
                    if max_width == 0:
                        break
        return max_area