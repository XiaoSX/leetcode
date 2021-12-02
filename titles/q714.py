#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-29
'''

# 贪心算法
# 巧妙在于用数组记录每时刻最佳状态
class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        buy = -99999
        sell = 0
        for p in prices:
            buy = max(buy, sell - p - fee)
            sell = max(sell, buy + p)
        return sell