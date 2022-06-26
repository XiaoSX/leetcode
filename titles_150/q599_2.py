#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/14
'''

from typing import List
# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         m = len(list1)
#         n = len(list2)
#
#         m_dict = {}
#         for i in range(m):
#             m_dict[list1[i]] = i
#
#         index_sum = m + n
#         ans = []
#         for i in range(n):
#             if list2[i] in m_dict:
#                 j = i + m_dict[list2[i]]
#                 if j < index_sum:
#                     index_sum = j
#                     ans = [list2[i]]
#                 elif j == index_sum:
#                     ans.append(list2[i])
#                 else:
#                     pass
#         return ans


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {s: i for i, s in enumerate(list1)}
        ans = []
        indexSum = inf
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [s]
                elif i + j == indexSum:
                    ans.append(s)
        return ans

