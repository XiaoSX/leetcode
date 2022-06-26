#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/15
'''

from typing import List
import numpy as np

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row_min = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            j = np.argmin(matrix[i])
            row_min.add((i, j))

        for j in range(n):
            i = np.argmax([matrix[x][j] for x in range(m)])
            if (i, j) in row_min:
                ans.append(matrix[i][j])
                return ans

        return ans
