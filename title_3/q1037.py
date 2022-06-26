#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/8
'''

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        xa, ya = a
        xb, yb = b
        xc, yc = c
        dx, dy = xb - xa, yb - ya
        dx2, dy2 = xc - xb, yc - yb
        if dx == 0 and dy == 0:
            return False
        if dx2 == 0 and dy2 == 0:
            return False
        if dy * dx2 == dy2 * dx:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    points = [[1, 1], [2, 3], [3, 2]]
    test.append(points)
    ans.append(True)

    points = [[1, 1], [2, 2], [3, 3]]
    test.append(points)
    ans.append(False)

    points = [[1, 1], [1, 1], [2, 3]]
    test.append(points)
    ans.append(False)

    points = [[1, 1], [1, 2], [1, 3]]
    test.append(points)
    ans.append(False)

    points = [[1, 1], [1, 2], [2, 3]]
    test.append(points)
    ans.append(True)

    for i in range(len(test)):
        assert s.isBoomerang(test[i]) == ans[i]