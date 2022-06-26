#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/1
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    ans += s[j]
                    j += 2 * numRows - 2
            else:
                j = i
                flag = False
                while j < len(s):
                    ans += s[j]
                    if flag:
                        j += 2 * i
                    else:
                        j += 2 * numRows - 2 - 2 * i
                    flag = not flag
        return ans


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         n, r = len(s), numRows
#         if r == 1 or r >= n:
#             return s
#         t = r * 2 - 2
#         ans = []
#         for i in range(r):  # 枚举矩阵的行
#             for j in range(0, n - i, t):  # 枚举每个周期的起始下标
#                 ans.append(s[j + i])  # 当前周期的第一个字符
#                 if 0 < i < r - 1 and j + t - i < n:
#                     ans.append(s[j + t - i])  # 当前周期的第二个字符
#         return ''.join(ans)
