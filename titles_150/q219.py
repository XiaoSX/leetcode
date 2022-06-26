#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/19
'''

from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        low = -k
        high = k - 1
        count = Counter(nums[max(low, 0):min(high + 1, n)])

        for i in range(n):
            if low >= 0:
                count[nums[low]] -= 1
            low += 1
            high += 1
            if high < n:
                count[nums[high]] += 1

            if count[nums[i]] >= 2:
                return True
        return False