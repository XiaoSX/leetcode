#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-07
'''

# array  二分分治递归的时候，如果low, high 下标不变，则要保证num必须传整体
# 如果下标变了，则必须把偏移带上
# case 2 如果只有一个元素的时候
# case 3 python 表示无穷小
class Solution:
    def subFind(self, nums, start_i):
        n = len(nums)
        if n <= 2:
            return -1

        low = 0
        high = n - 1
        mid = (low + high) // 2
        if mid - 1 >= 0 and mid + 1 <= high and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return start_i + mid

        pre_half = self.subFind(nums[:mid + 1], start_i)
        if pre_half >= 0:
            return pre_half
        return self.subFind(nums[mid:], start_i + mid)

    def findPeakElement(self, nums) -> int:
        return self.subFind([float('-inf')] + nums + [float('-inf')], 0) - 1