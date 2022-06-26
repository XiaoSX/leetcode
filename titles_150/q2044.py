#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/15
'''

from typing import List

class Solution:
    def __init__(self):
        self.max_v = 0
        self.ans = 0

    def search(self, arr, sub_set):
        n = len(arr)
        if n == 0:
            if sub_set > self.max_v:
                self.max_v = sub_set
                self.ans = 1
            elif sub_set == self.max_v:
                self.ans += 1
            else:
                pass
            return

        self.search(arr[1:], sub_set)
        self.search(arr[1:], sub_set | arr[0])
        return

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        sub_set = 0
        self.search(nums, sub_set)
        return self.ans
