#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/19
'''

from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        # i应该放在i-1位置上
        for i in range(n, 1, -1):
            j = arr.index(i)
            if j == i - 1:
                continue

            if j != 0:
                ans.append(j+1)
                arr = arr[:j+1][::-1] + arr[j+1:]

            ans.append(i)
            arr = arr[:i][::-1] + arr[i:]

        return ans