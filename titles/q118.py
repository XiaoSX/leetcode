#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-27
'''

class Solution:
    def generate(self, numRows: int):
        # if numRows == 0:
        #     return [[]]
        # ans = [[1]]
        # for i in range(1, numRows):
        #     _ans = [1]
        #     for j in range(len(ans[-1]) - 1):
        #         _ans.append(ans[-1][j] + ans[-1][j + 1])
        #     _ans.append(1)
        #     ans.append(_ans)
        # return ans
        ans = [[1]]
        while len(ans) < numRows:
            newRow = [a + b for a, b in zip([0] + ans[-1], ans[-1] + [0])]
            ans.append(newRow)
        return ans
