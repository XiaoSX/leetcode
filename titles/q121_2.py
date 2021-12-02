#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-27
'''

class Solution:
    def maxProfit(self, prices) -> int:
        buy = -99999
        sell = 0
        for p in prices:
            buy = max(buy, -p)
            sell = max(sell, buy + p)
        return sell