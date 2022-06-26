#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/30
'''


"""
n = [[1, 2], [3, 4]]
"""


def rotateArray(nums):
    n = len(nums)
    for i in range(n // 2 + 1):
        for j in range(i, n - i - 1):
            ci, cj = i, j
            cur = nums[ci][cj]
            for k in range(4):
                ni, nj = cj, n - ci - 1
                tmp = nums[ni][nj]
                nums[ni][nj] = cur
                cur = tmp
                ci = ni
                cj = nj
