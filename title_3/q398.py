#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/25
'''

from typing import List
from random import randrange
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        ans = -1
        for i, cur in enumerate(self.nums):
            if cur == target:
                cnt += 1
                if randrange(cnt) == 0:
                    ans = i
        return ans
