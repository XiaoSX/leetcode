#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/26
'''

from typing import List
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        zxArea = sum(map(max, grid))
        return xyArea + yzArea + zxArea


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append([[1,2],[3,4]])
    ans.append(17)
    test.append([[2]])
    ans.append(5)
    test.append([[1,0],[0,2]])
    ans.append(8)
    for i in range(len(test)):
        assert s.projectionArea(test[i]) == ans[i]
