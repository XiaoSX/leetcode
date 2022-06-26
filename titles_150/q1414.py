#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/3
'''
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 1:
            return 1

        nums = [1, 1]
        while nums[-1] < k:
            nums.append(nums[-1] + nums[-2])
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            if k == nums[i]:
                cnt += 1
                break
            elif k > nums[i]:
                k -= nums[i]
                cnt += 1
        return cnt