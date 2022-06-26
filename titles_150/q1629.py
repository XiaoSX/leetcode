#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/9
'''

from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time = 0
        max_char = ''
        for i in range(len(keysPressed)):
            t = keysPressed[i]
            if i == 0:
                max_time = releaseTimes[i]
                max_char = t
                continue
            if releaseTimes[i] - releaseTimes[i - 1] > max_time:
                max_time = releaseTimes[i] - releaseTimes[i - 1]
                max_char = t
            elif releaseTimes[i] - releaseTimes[i - 1] == max_time and t > max_char:
                max_char = t
        return max_char
