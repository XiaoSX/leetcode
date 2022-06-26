#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/14
'''

from typing import List

# 单个元素是奇偶下标的分界, 单个元素前，下标都是偶数开始，后，下标变为奇数开始
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # 偶数下标开始，没有遇到单个值
            # mid 奇数，比较（mid， mid-1）
            # mid 偶数，比较（mid， mid + 1）
            # 即比较 （mid， mid ^ 1）
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

# # 单个元素是奇偶下标的分界, 单个元素前，下标都是偶数开始，后，下标变为奇数开始
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         low, high = 0, len(nums) - 1
#         while low < high:
#             mid = (low + high) // 2
#             # 偶数下标
#             # mid 奇数，搞成偶数 mid - 1
#             # mid 偶数，不变
#             # 即 mid -= mid & 1
#             mid -= mid & 1
#             if nums[mid] == nums[mid + 1]:
#                 low = mid + 2
#             else:
#                 high = mid
#         return nums[low]

