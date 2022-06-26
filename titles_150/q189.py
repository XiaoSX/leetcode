#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-23
'''

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # 前部
        pl, ph = 0, n - k - 1
        # 后部
        ll, lh = n - k, n - 1
        # 前部和后部都不为空
        while pl <= ph and ll <= lh:
            i = pl
            j = ll
            # 交换前后部分
            while i <= ph and j <= lh:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            # 交换完成
            if i > ph and j > lh:
                pl = ph + 1
                ll = lh + 1
            # 前部分没有交换完，后部分继续和剩余的前部分交换
            if i <= ph:
                pl = i
            # 后部分没有交换完，后部分的前部分和剩余后部分继续交换
            elif j <= lh:
                pl, ph = ll, j - 1
                ll = j
