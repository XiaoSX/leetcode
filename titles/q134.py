#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-01
'''

# 关键在于什么时候更新出发点, 走不动的时候再更新
# 在耗油量最低的时候更新出发点
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        cum = 0   # 全局负荷量
        start = -1
        remain = -1   # 走不动

        for i in range(len(gas)):
            delta = gas[i] - cost[i]
            if remain < 0 and delta >= 0:
                start = i
                remain = 0
            remain += delta
            cum += delta

        if cum < 0:
            return -1
        else:
            return start
