#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/8
'''

from typing import List
from collections import Counter

def bi_search(arr, num):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            high = mid
        else:
            low = mid + 1
    return low


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        indexs = []
        for i in range(len(s)):
            if s[i] == '|':
                indexs.append(i)

        ans = []
        for q in queries:
            left, right = q
            li = bi_search(indexs, left)
            if li == len(indexs):
                ans.append(0)
                continue
            lbound = indexs[li]
            ri = bi_search(indexs, right)
            if ri == li:
                ans.append(0)
                continue
            if ri == len(indexs) or indexs[ri] > right:
                rbound = indexs[ri-1]
                ans.append(max(rbound - lbound + 1 - (ri - li), 0))
            else:
                rbound = indexs[ri]
                ans.append(max(rbound - lbound + 1 - (ri - li + 1), 0))


        return ans