#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/22
'''

from typing import List
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n == 1:
            return 0

        stockPrices = sorted(stockPrices, key=lambda x:x[0])

        x2, y2 = stockPrices[1]
        x1, y1 = stockPrices[0]
        dx1, dy1 = x2 - x1, y2 - y1
        cnt = 1
        for i in range(2, n):
            x2, y2 = stockPrices[i]
            x1, y1 = stockPrices[i - 1]
            dx2, dy2 = x2 - x1, y2 - y1
            if dy2 * dx1 != dy1 * dx2:
                cnt += 1
                dx1, dy1 = dx2, dy2
        return cnt


if __name__ == '__main__':
    points = [[72, 98], [62, 27], [32, 7], [71, 4], [25, 19], [91, 30], [52, 73], [10, 9], [99, 71], [47, 22], [19, 30],
     [80, 63], [18, 15], [48, 17], [77, 16], [46, 27], [66, 87], [55, 84], [65, 38], [30, 9], [50, 42], [100, 60],
     [75, 73], [98, 53], [22, 80], [41, 61], [37, 47], [95, 8], [51, 81], [78, 79], [57, 95]]
    s = Solution()
    ans = s.minimumLines(points)
    assert ans == 29
    points = [[1, 1]]
    ans = s.minimumLines(points)
    assert ans == 0
    points = [[3,4],[1,2],[7,8],[2,3]]
    ans = s.minimumLines(points)
    assert ans == 1
    points = [[3, 4], [1, 2]]
    ans = s.minimumLines(points)
    assert ans == 1
