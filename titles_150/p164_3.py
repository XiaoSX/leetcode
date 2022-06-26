#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-13
'''

class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0

        max_v = max(nums)
        base = 1
        while base <= max_v:
            digit_array = [0 for _ in range(10)]
            for cur in nums:
                digit = int(cur / base % 10)
                digit_array[digit] += 1
            for i in range(1, 10):
                digit_array[i] += digit_array[i - 1]
            new_array = [0 for _ in range(n)]
            for i in range(n-1, -1, -1):
                digit = int(nums[i] / base % 10)
                new_array[digit_array[digit] - 1] = nums[i]
                digit_array[digit] -= 1
            nums = list(new_array)
            base *= 10
        max_margin = 0
        for i in range(1, n):
            max_margin = max(max_margin, nums[i] - nums[i - 1])
        return max_margin
