#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/13
'''

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return False

        m1, m2 = float('inf'), float('inf')
        for item in nums:
            if item > m2:
                return True

            if item > m1:
                m2 = item
            else:
                m1 = item


            if item < m1:
                m1 = item
            elif item > m1:
                m2 = item
        return False