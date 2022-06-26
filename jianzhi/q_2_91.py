#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/25
'''

from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        d = [0, 0, 0]
        for i in range(n):
            _d0 = min(d[1], d[2]) + costs[i][0]
            _d1 = min(d[0], d[2]) + costs[i][1]
            _d2 = min(d[0], d[1]) + costs[i][2]
            d = [_d0, _d1, _d2]

        return min(d)


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    test.append(costs)
    ans.append(10)
    costs = [[7, 6, 2]]
    test.append(costs)
    ans.append(2)
    for i in range(len(test)):
        assert s.minCost(test[i]) == ans[i]



