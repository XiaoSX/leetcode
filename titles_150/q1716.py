#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/15
'''

class Solution:
    def totalMoney(self, n: int) -> int:
        circles = n // 7
        mode = n % 7

        totals = 0
        totals += 28 * circles + circles * (circles - 1) // 2 * 7
        for i in range(1, mode+1):
            totals += circles + i

        return totals