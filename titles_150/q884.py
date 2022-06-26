#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/30
'''

from typing import List
from collections import Counter

# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         s1 = s1.split(' ')
#         s2 = s2.split(' ')
#         count_s1 = Counter(s1)
#         count_s2 = Counter(s2)
#         ans = []
#         for k in count_s1:
#             if count_s1[k] == 1 and k not in count_s2:
#                 ans.append(k)
#
#         for k in count_s2:
#             if count_s2[k] == 1 and k not in count_s1:
#                 ans.append(k)
#
#         return ans

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = Counter(s1.split()) + Counter(s2.split())

        ans = list()
        for word, occ in freq.items():
            if occ == 1:
                ans.append(word)

        return ans
