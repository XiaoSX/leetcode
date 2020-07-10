#  -*-  coding: utf-8  -*-

INT_MIN = -2147483648
INT_MAX = 2147483647

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 越界问题只会发生在除1和-1
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > INT_MIN:
                return -dividend
            return INT_MAX

        sign_dent = -1 if dividend < 0 else 1
        sign_sor = -1 if divisor < 0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if sign_dent == sign_sor:
            sign_ans = 1
        else:
            sign_ans = -1

        res = 0
        remain = dividend
        while remain >= divisor:
            cnt = 1
            ans = divisor
            while ans + ans < remain:
                ans += ans
                cnt *= 2
            res += cnt
            remain = remain - ans
        if sign_ans < 0:
            res = 0 - res

        return res