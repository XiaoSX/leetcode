#  -*-  coding: utf-8  -*-
class Solution:
    def myPow(self, x: float, n: int) -> float:

        sign = 1
        if n < 0:
            sign = -1
            n = abs(n)

        total = 1
        x_contribute = x
        while n > 0:
            if n % 2 == 1:
                total *= x_contribute
            x_contribute *= x_contribute
            n = n // 2

        if sign < 0:
            total = 1 * 1.0 / total

        return total