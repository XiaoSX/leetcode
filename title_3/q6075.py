#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/22
'''

from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [capacity[i] - rocks[i] for i in range(len(capacity))]
        diff = sorted(diff)
        cnt = 0
        for i in range(len(capacity)):
            cnt += diff[i]
            if cnt == additionalRocks:
                return i + 1
            if cnt > additionalRocks:
                return i

        return len(capacity)

if __name__ == '__main__':
    c = [91, 54, 63, 99, 24, 45, 78]
    r = [35, 32, 45, 98, 6, 1, 25]
    addi = 17
    s = Solution()
    s.maximumBags(c, r, addi)