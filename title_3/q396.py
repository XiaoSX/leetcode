#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/22
'''

from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        max_v = max(float('-inf'), f)
        for i in range(1, n):
            max_v = max(max_v, f + tmp - n * nums[n - i])
            f = f + tmp - n * nums[n - i]

        return max_v

if __name__ == '__main__':
    s = Solution()
    arr = [1,2,3,4,5,6,7,8,9,10]
    s.maxRotateFunction(arr)