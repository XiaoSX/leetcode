#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/29
'''

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         s_dict = {}
#         low = 0
#         high = 0
#         max_len = 0
#         n = len(s)
#
#         for i in range(n):
#             if s[i] not in s_dict or s_dict[s[i]] < low:
#                 high = i + 1
#                 max_len = max(max_len, high - low)
#             else:
#                 low = s_dict[s[i]] + 1
#             s_dict[s[i]] = i
#         return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res