#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/25
'''

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        stack = []
        n = len(nums)

        for i in range(n):
            if i >= k:
                ans.append(stack[0])
                stack = stack[1:]

            cur = nums[i]
            for j in range(len(stack) - 1, -1, -1):
                if stack[j] < cur:
                    stack[j] = cur
                else:
                    break
            stack.append(cur)
        if len(stack) > 0:
            ans.append(stack[0])
        return ans



