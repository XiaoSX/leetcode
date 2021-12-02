#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-19
'''

class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        candys = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candys[i] = candys[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candys[i] = max(candys[i], candys[i + 1] + 1)

        return sum(candys)