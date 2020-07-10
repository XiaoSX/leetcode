#  -*-  coding: utf-8  -*-
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        max_INT = 2147483647
        min_INT = -2147483648

        s = re.sub('^\s+', '', s)
        n = len(s)
        if n == 0:
            return 0
        if s[0] not in '0123456789-+':
            return 0
        sign = '+'
        if s[0] in '+-':
            sign = s[0]
            s = s[1:]
        numbers = []
        for i in range(len(s)):
            if s[i] not in '0123456789':
                break
            numbers.append(int(s[i]))

        n = len(numbers)
        totals = 0
        tmp = 1
        for i in range(n - 1, -1, -1):
            totals += numbers[i] * tmp
            tmp *= 10

        totals = totals if sign == '+' else -totals
        if totals > 0:
            return min(totals, max_INT)
        else:
            return max(totals, min_INT)


