#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/15
'''

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        final_ans = []

        def combine(arr, m, ans):
            if len(arr) < m:
                return

            if m == 0:
                final_ans.append(list(ans))
                return

            if m == len(arr):
                final_ans.append(list(ans) + arr)
                return

            combine(arr[1:], m - 1, ans + [arr[0]])
            combine(arr[1:], m, ans)
        combine(list(range(n)), 3, [])
        max_area = 0
        for ps in final_ans:
            i, j, k = ps
            a, b, c = points[i], points[j], points[k]
            ax, ay = a[0] - c[0], a[1] - c[1]
            bx, by = b[0] - c[0], b[1] - c[1]
            area = abs(ax * by - ay * bx)
            if area > max_area:
                max_area = area

        return max_area / 2


if __name__ == '__main__':
    s = Solution()
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    points = [[1, 0], [0, 0], [0, 1]]
    print(s.largestTriangleArea(points))