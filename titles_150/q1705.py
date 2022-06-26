#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-24
'''
from queue import PriorityQueue

class Solution:
    def eatenApples(self, apples, days) -> int:
        day_apples = PriorityQueue()

        n = len(apples)
        cnt = 0
        for i in range(n):
            if apples[i] != 0:
                day_apples.put((i + days[i] - 1, apples[i]))

            min_k = None
            min_v = None
            while not day_apples.empty():
                min_k, min_v = day_apples.get()
                if min_k >= i:
                    break

            if min_k is None or min_k < i:
                continue

            if min_v - 1 > 0:
                day_apples.put((min_k, min_v - 1))
            cnt += 1

        pre_day = n - 1
        pre_apple = 0
        total_day_cnt = 0
        while not day_apples.empty():
            y_day, y_apples = day_apples.get()

            day_cnt = y_day - pre_day
            pre_day = y_day
            pre_apple = min(0, y_apples + pre_apple - day_cnt)
            total_day_cnt += day_cnt
        cnt += total_day_cnt + pre_apple

        return cnt

