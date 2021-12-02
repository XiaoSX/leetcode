# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 上午11:38
# @Author  : RenMeng
# @File    : q123.py

class Solution:
    # policy: buy_in when min_price; buy_out when max_price
    # 最低点买入, 最高点卖出
    def maxProfit(self, prices) -> int:
        # 收集所有买入卖出点
        if len(prices) == 0:
            return 0

        buy_in = []
        sell_out = []

        i = 0
        n = len(prices)
        while i < n - 1:
            while i < n - 1 and prices[i + 1] <= prices[i]:
                i += 1
            if i == n - 1:
                continue
            else:
                buy_in.append(prices[i])
                i += 1
            while i < n - 1 and prices[i + 1] >= prices[i]:
                i += 1
            sell_out.append(prices[i])
            i += 1

        assert len(buy_in) == len(sell_out)

        n = len(sell_out)
        # profits[i][j]: 以j为出售点, i点后的max_profit, i <= j
        profits = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            profits[i][i] = sell_out[i] - buy_in[i]


        for i in range(n):
            for j in range(i + 1, n):
                profits[i][j] = sell_out[j] - sell_out[j - 1] + profits[i][j - 1]
                profits[i][j] = max(profits[i][j], profits[j][j])

        max_sum = 0
        for i in range(n):
            # i, j 为选定的卖出点
            profit1 = profits[0][i]
            profit2 = 0
            for j in range(i + 1, n):
                profit2 = profits[i + 1][j]
                if max_sum < (profit1 + profit2):
                    max_sum = profit1 + profit2
            if max_sum < (profit1 + profit2):
                max_sum = profit1 + profit2
        return max_sum

