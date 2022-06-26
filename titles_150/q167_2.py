#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/31
'''
class Solution:
    def twoSum(self, numbers, target: int):
        n = len(numbers)
        p = 0
        q = n - 1
        while p < q:
            while p < q and numbers[p] + numbers[q] > target:
                q -= 1
            while p < q and numbers[p] + numbers[q] < target:
                p += 1
            if numbers[p] + numbers[q] == target:
                return [p + 1, q + 1]