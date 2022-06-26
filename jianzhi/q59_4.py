#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/26
'''

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        prefix = []
        suffix = []
        cur_group = []
        for i in range(n // k + 1):
            _prefix = []
            max_v = float('-inf')
            for j in range(k):
                p = i * k + j
                if p >= n:
                    break
                if nums[p] > max_v:
                    max_v = nums[p]
                _prefix.append(max_v)

            if len(_prefix) > 0:
                prefix.append(_prefix)
                cur_group.append(max_v)
                _suffix = []
                max_v = float('-inf')
                for j in range(k-1, -1, -1):
                    p = i * k + j
                    if p >= n:
                        _suffix.append(float('-inf'))
                        continue
                    if nums[p] > max_v:
                        max_v = nums[p]
                    _suffix.append(max_v)
                suffix.append(_suffix)

        ans = []
        for i in range(n - k + 1):
            if i % k == 0:
                ans.append(cur_group[i // k])
            else:
                suf = suffix[i // k][k - i % k - 1]
                max_v = suf
                if i // k + 1 < len(prefix):
                    pre = prefix[i // k + 1][i % k - 1]
                    max_v = max(max_v, pre)
                ans.append(max_v)

        return ans