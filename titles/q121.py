# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 上午10:24
# @Author  : RenMeng
# @File    : q121.py

# greedy
class Solution:
    def maxProfit(self, prices) -> int:
        buy_in = 999999
        interest = 0

        # 当前price比买入时候低,则更新买入；else tell me 卖出赚多少钱；return the max interest
        for money in prices:
            if money > buy_in:
                interest = max(interest, money - buy_in)
            elif money < buy_in:
                buy_in = money

        return interest