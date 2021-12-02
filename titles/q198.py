#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-06
'''


class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        p_no = 0
        p = nums[0]

        for i in range(1, n):
            p_no_2 = max(p_no, p)
            p = p_no + nums[i]
            p_no = p_no_2

        return max(p_no, p)