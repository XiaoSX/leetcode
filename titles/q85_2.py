# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 上午10:50
# @Author  : RenMeng
# @File    : q85_2.py

class Solution:
    # 每个点的最左最右边界, 以及height
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        heights = [0 for _ in range(n)]
        lefts = [0 for _ in range(n)]
        rights = [n for _ in range(n)]
        max_area = 0
        for i in range(m):
            cur_left = -1
            cur_right = n
            # 遍历一趟就可以确定当前点的最左或最右边界
            # 依次遍历当前点,就可得到全局最优
            # 最右(最左) = cur最右和累计最右的min
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                    lefts[j] = max(lefts[j], cur_left + 1)
                else:
                    heights[j] = 0
                    lefts[j] = 0
                    cur_left = j
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    rights[j] = min(cur_right, rights[j])
                else:
                    cur_right = j
                    rights[j] = n

            for j in range(n):
                max_area = max(max_area, heights[j] * (rights[j] - lefts[j]))
        return max_area