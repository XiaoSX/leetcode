# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 上午10:36
# @Author  : RenMeng
# @File    : q122.py


class Solution:
    # policy: buy_in when min_price; buy_out when max_price
    # 最低点买入, 最高点卖出
    def maxProfit(self, prices) -> int:
        buy_in = 999999
        interest = 0
        buy_out = -1 # 0是valid_value
        i = 0

        # 很容易漏掉循环结束时候的更新操作, 此题不需要, 因为buy_in 更新后, buy_out也需要更新, 才能计算interest
        # buy_in buy_out 每轮结束后, 需必要适时更新, 因为不是全局变量
        while i < len(prices):
            # 买入点
            # 临界 买入点是交易最后一天
            # 循环存在找不到的情况
            while i < len(prices) and prices[i] < buy_in:
                buy_in = prices[i]
                i += 1
            # 卖出点
            while i < len(prices) and prices[i] > buy_out:
                buy_out = prices[i]
                i += 1

            # 找不到 卖出点, 交易结束
            if buy_out == -1:
                break

            # 存在卖出点, 交易
            interest += (buy_out - buy_in)

            # 找不到买入点
            if i >= len(prices):
                break

            # 存在买入点, 更新值,继续交易
            # 继续交易, 更新buy_in, buy_out
            buy_out = -1
            buy_in = prices[i]
            i += 1
        return interest
