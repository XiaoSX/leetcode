#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/26
'''

import heapq
from typing import List

# 牛逼
# heapq 并不删除, 所有元素入队, 当前元素不再有效坐标范围内, 在pop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        n = len(nums)

        ans.append(-q[0][0])
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

