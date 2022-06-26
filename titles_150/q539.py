#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/18
'''

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24 * 60:
            return 0
        timePoints = [x.split(':') for x in timePoints]
        timePoints = [[int(x[0]), int(x[1])] for x in timePoints]
        timePoints = sorted(timePoints, key=lambda x: [x[0], x[1]])
        min_ans = 24 * 60
        for i in range(len(timePoints)-1):
            hour, minute = timePoints[i]
            nhour, nminute = timePoints[(i+1)%len(timePoints)]
            gap = (nhour - hour) * 60 + nminute - minute
            if gap < min_ans:
                min_ans = gap
        last_m = (24 - timePoints[-1][0]) * 60 - timePoints[-1][1] + timePoints[0][0] * 60 + timePoints[0][1]
        min_ans = min(min_ans, last_m)
        return min_ans