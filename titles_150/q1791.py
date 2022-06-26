#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/18
'''

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x, y = edges[0]
        if x in edges[1]:
            return x
        else:
            return y
