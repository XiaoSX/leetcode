#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-27
'''

class Solution:
    # policy: buy_in when min_price; buy_out when max_price
    # u不放过任何一笔利润
    def maxProfit(self, prices) -> int:
        profits = 0
        buy = 99999
        for p in prices:
            if p < buy:
                buy = p
            else:
                profits += p - buy
                buy = p
        return profits