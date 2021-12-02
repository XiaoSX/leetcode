#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-26
'''


class Solution:
    # policy: buy_in when min_price; buy_out when max_price
    # 最低点买入, 最高点卖出
    def maxProfit(self, prices) -> int:
        # 收集所有买入卖出点
        fstbuy = -99999
        fstsell = 0
        secbuy = -99999
        secsell = 0

        for p in prices:
            fstbuy = max(fstbuy, -p)  # 第一次买 - p
            fstsell = max(fstsell, fstbuy + p)   # 第一次卖fstbut + p
            secbuy = max(secbuy, fstsell - p)   # 第一次卖了后现在买fstsell - p
            secsell = max(secsell, secbuy + p)   # 第二次买了后现在卖secbuy + p

        return secsell