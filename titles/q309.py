#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-29
'''

class Solution:
    def maxProfit(self, prices) -> int:
        buy_has = -99999
        buy_no = -99999
        sell_has = 0
        sell_no = 0
        # 维护如果当天买入, 则发生交易的当前时刻最大值；
        # 如果当天不买入, 则当前买入的max, 应该是前一天买入的, 和前一天不买入的max
        # 贪心
        # buy_{4_has} = sell_{3_no} - p_{4}
        # buy_{4_no} = max(buy_{3_no}, buy_{3_has})

        # sell_{4_has} = max(buy_{4_has} + p, buy_{4_no} + p) 当天有交易, max和当天的买入有关, 因为是当天发生的卖出交易,
        # 所以这之前的任何一天都可以买入
        # sell_{4_no} = max(sell_{3_no}, sell_{3_has}) 当天没有交易, max收入只和前一天有关, 前一天可以有,也可以没有交易

        # 方法二: 分清前一天是否有买卖状态即可, 三种状态: 买入, 卖出(昨天), 卖出(非昨天), 交易以卖出为准, 故买入不需要区分状态
        for p in prices:
            buy_has_new = sell_no - p
            buy_no = max(buy_has, buy_no)
            buy_has = buy_has_new

            sell_no = max(sell_no, sell_has)
            sell_has = max(buy_no + p, buy_has + p)

        return max(sell_has, sell_no)