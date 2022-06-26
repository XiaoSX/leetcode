#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/16
'''

from typing import List
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        n = len(operations)
        min_v = float('inf')
        max_v = float('-inf')
        for j in range(n):
            x, y = operations[j]
            give = gem[x] // 2
            gem[x] -= give
            gem[y] += give

        for i in range(len(gem)):
            min_v = min(gem[i], min_v)
            max_v = max(gem[i], max_v)

        return max_v - min_v


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    gem = [3, 1, 2]
    operations = [[0, 2], [2, 1], [2, 0]]
    test.append([gem, operations])
    ans.append(2)
    gem = [100, 0, 50, 100]
    operations = [[0, 2], [0, 1], [3, 0], [3, 0]]
    test.append([gem, operations])

    ans.append(75)
    gem = [0, 0, 0, 0]
    operations = [[1, 2], [3, 1], [1, 2]]
    test.append([gem, operations])

    ans.append(0)

    for i in range(len(test)):
        assert s.giveGem(*test[i]) == ans[i]