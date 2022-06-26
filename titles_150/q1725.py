#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/4
'''

from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        count = 0
        for p in rectangles:
            x = min(p)
            if x == max_len:
                count += 1
            elif x > max_len:
                max_len = x
                count = 1
        return count