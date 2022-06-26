#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/14
'''

from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ans = []
        flag = True
        for i in range(m + n):
            if not flag:
                # 从上到下, 对角线和=i, init元素(0, i), 依次row+1, col-1
                for j in range(min(n - 1, i), max(i - m, -1), -1):
                    ans.append(mat[i - j][j])
            else:
                # 从下到上, 对角线和=i, init元素(i, 0), 依次row-1, col+1
                for j in range(min(m - 1, i), max(i - n, -1), -1):
                    ans.append(mat[j][i - j])
            # flag = ~flag
            flag = not flag
        # print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    test.append(mat)
    ans.append([1, 2, 4, 7, 5, 3, 6, 8, 9])
    mat = [[1, 2], [3, 4]]
    test.append(mat)
    ans.append([1, 2, 3, 4])
    for i in range(len(test)):
        assert s.findDiagonalOrder(test[i]) == ans[i]