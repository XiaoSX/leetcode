#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-27
'''

class Solution:
    # policy: buy_in when min_price; buy_out when max_price
    # 最低点买入, 最高点卖出
    def maxProfit(self, prices) -> int:
        firstbuy = -99999
        firstsell = 0
        secondbuy = -99999
        secondsell = 0

        for p in prices:
            firstbuy = max(firstbuy, -p)
            firstsell = max(firstsell, firstbuy + p)
            secondbuy = max(secondbuy, firstsell - p)
            secondsell = max(secondsell, secondbuy + p)

        return secondsell