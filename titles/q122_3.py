#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-27
'''

class Solution:
    # policy: buy_in when min_price; buy_out when max_price
    # u不放过任何一笔利润, 一笔最高利润, 多笔为贪心, 不放过任何利润
    def maxProfit(self, prices) -> int:
        sell = 0
        buy = -99999
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p)
        return sell