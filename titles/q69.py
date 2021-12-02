# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 下午3:01
# @Author  : RenMeng
# @File    : q69.py

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)
