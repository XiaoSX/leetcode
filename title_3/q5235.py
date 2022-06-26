#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/3
'''

from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        n = len(matches)
        count = [[0, 0] for _ in range(100001)]
        for i in range(n):
            win, lose = matches[i]
            count[win][0] += 1
            count[lose][1] += 1

        ans_0 = []
        ans_1 = []
        for i in range(100001):
            if count[i][0] > 0 and count[i][1] == 0:
                ans_0.append(i)
            if count[i][1] == 1:
                ans_1.append(i)

        return [ans_0, ans_1]


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    y = [[1, 2, 10], [4, 5, 7, 8]]
    test.append(matches)
    ans.append(y)
    matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    y = [[1, 2, 5, 6], []]
    test.append(matches)
    ans.append(y)
    matches = [[1,100000]]
    y = [[1], [100000]]
    for i in range(len(test)):
        assert s.findWinners(test[i]) == ans[i]