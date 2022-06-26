#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/21
'''
from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        records = set()
        for num in nums:
            if num in records:
                return num
            records.add(num)
