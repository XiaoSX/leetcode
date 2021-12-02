# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 上午11:01
# @Author  : RenMeng
# @File    : q53.py

class Solution:
    def maxSubArray(self, nums) -> int:
        max_v = -999999
        f = 0
        for num in nums:
            f = f + num if f > 0 else num
            if f > max_v:
                max_v = f
        return max_v