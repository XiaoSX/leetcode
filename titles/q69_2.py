# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 下午4:39
# @Author  : RenMeng
# @File    : q69_2.py

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1