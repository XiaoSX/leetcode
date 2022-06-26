#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/13
'''

from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m = max(heights)
        cnt = [0] * (m + 1)

        for h in heights:
            cnt[h] += 1

        # height[idx] 里应该是按照高度排的序
        idx = ans = 0
        for i in range(m + 1):
            for j in range(cnt[i]):
                # 如果当前值, 不是高度i, 记录
                if heights[idx] != i:
                    ans += 1
                idx += 1

        return ans


