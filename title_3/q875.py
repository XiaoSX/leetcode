#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/7
'''

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        low = 1
        high = piles[-1] + 1
        while low < high:
            mid = (low + high) // 2
            need_hour = sum([1 if x <= mid else (x - 1) // mid + 1 for x in piles])
            if need_hour > h:
                low = mid + 1
            else:
                high = mid
        return high


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    piles = [3, 6, 7, 11]
    h = 8
    test.append([piles, h])
    ans.append(4)

    piles = [30, 11, 23, 4, 20]
    h = 5
    test.append([piles, h])
    ans.append(30)

    piles = [30, 11, 23, 4, 20]
    h = 6
    test.append([piles, h])
    ans.append(23)

    piles = [1, 2, 800, 1000]
    h = 4
    test.append([piles, h])
    ans.append(1000)

    piles = [312884470]
    h = 312884469
    test.append([piles, h])
    ans.append(2)

    for i in range(len(test)):
        assert s.minEatingSpeed(*test[i]) == ans[i]