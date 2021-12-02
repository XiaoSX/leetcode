#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-28
'''

class Solution:
    def __init__(self):
        self.sum = float('inf')

    def search(self, t, depth, coor, total):
        index, col = coor
        if depth == index:
            if self.sum > total:
                self.sum = total
            return

        total += t[index][col]
        self.search(t, depth, (index + 1, col), total)
        self.search(t, depth, (index + 1, col + 1), total)
        total -= t[index][col]
        return



    def minimumTotal(self, triangle) -> int:
        depth = len(triangle)
        self.search(triangle, depth, (0, 0), 0)
        return self.sum