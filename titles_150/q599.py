#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/14
'''

from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = len(list1)
        n = len(list2)

        ans = []
        for i in range(m + n - 1):
            for j in range(min(i+1, m)):
                a = list1[j]
                if i - j < 0 or i - j >= n:
                    continue
                b = list2[i-j]
                if a == b:
                    ans.append(a)
            if len(ans) > 0:
                return ans
        return ans
