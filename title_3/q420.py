#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/2
'''


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        if n < 6:
            return 6 - n

        i = 0
        is_lower = False
        is_capital = False
        is_digit = False
        pri = ''
        pri_num = 0
        ans = 0
        while n > 20:
            cur = password[i]
            i += 1
            if i - ans > 20:
                ans += 1
                n -= 1

            if cur == pri and pri_num < 2:
                pri_num += 1
            elif cur == pri:
                ans += 1
                n -= 1
            else:
                pri = cur
                pri_num = 0

            if not is_lower:
                if cur.islower():
                    is_lower = True

            if not is_capital:
                if cur.isupper():
                    is_capital = True

            if not is_digit:
                if cur.isdigit():
                    is_digit = True

