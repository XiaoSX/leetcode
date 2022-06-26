#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/1
'''
from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        N = len(original)
        if N != m * n:
            return []

        tmp = []
        for i in range(N):
            tmp.append(original[i])
            if len(tmp) == n:
                ans.append(tmp[:])
                tmp = []
        return ans