#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/25
'''

from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low_i = 0
        low_j = 0
        high_i = m
        high_j = n
        while low_i < high_i and low_j < high_j:
            if target < matrix[low_i][low_j] or target > matrix[high_i - 1][high_j - 1]:
                return False
            if target == matrix[low_i][low_j] or target == matrix[high_i - 1][high_j - 1] or \
                target == matrix[low_i][high_j - 1]:
                return True

            if target > matrix[low_i][high_j - 1]:
                low = low_i + 1
                high = high_i
                while low < high:
                    mid = (low + high) // 2
                    if matrix[mid][high_j - 1] == target:
                        return True
                    if matrix[mid][high_j - 1] < target:
                        low = mid + 1
                    else:
                        high = mid
                low_i = low
            else:
                low = low_j
                high = high_j
                while low < high:
                    mid = (low + high) // 2
                    if matrix[low_i][mid] == target:
                        return True
                    if matrix[low_i][mid] < target:
                        low = mid + 1
                    else:
                        high = mid
                high_j = low
        return False