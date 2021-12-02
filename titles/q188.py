#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-31
'''

class Solution:
    def maxProfit(self, k: int, prices) -> int:
        buys = [-99999 for _ in range(k)]
        sells = [0] + [0 for _ in range(k)]
        for p in prices:
            for i in range(k):
                buys[i] = max(buys[i], sells[i] - p)
                sells[i + 1] = max(sells[i + 1], buys[i] + p)
        return sells[-1]