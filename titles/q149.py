#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-03
'''
from collections import defaultdict

# 枚举通过当前点的所有方向上点的个数即可，o(n^2)
class Solution:
    def maxPoints(self, points) -> int:
        n = len(points)
        if n == 0 or n == 1:
            return n

        points_dir = [set() for _ in range(n)]

        max_v = 0
        for i in range(n):
            direction = defaultdict(lambda: 1)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = float('inf')
                if x1 != x2:
                    dx = (y2 - y1) / (x2 - x1)
                points_dir[j].add(dx)
                if dx not in points_dir[i]:
                    direction[dx] += 1

            for k in direction:
                max_v = max(max_v, direction[k])

        return max_v


