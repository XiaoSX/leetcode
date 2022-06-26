#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/13
'''

from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = 0
        flag = True   # 是否找到最大
        for i in range(1, n):
            item = nums[i]
            # 最大值 > 遇到的值两倍
            if 2 * item <= nums[max_i]:
                flag = True & flag
            # 遇到最大 是最大
            elif item >= 2 * nums[max_i]:
                flag = True
                max_i = i
            # 遇到最大 不是最大
            elif item > nums[max_i]:
                flag = False
                max_i = i
            else:
                flag = False
        return max_i if flag else -1
