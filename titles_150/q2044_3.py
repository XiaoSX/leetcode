#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/15
'''

from functools import reduce
from typing import List
from operator import or_

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0
        for i in range(1, 1 << len(nums)):
            orVal = reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
            if orVal > maxOr:
                maxOr, cnt = orVal, 1
            elif orVal == maxOr:
                cnt += 1
        return cnt
