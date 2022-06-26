#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/8
'''

# class Solution:
#     def grayCode(self, n: int):
#         ans = [0, 1]
#         for i in range(2, n+1):
#             high_j = len(ans)
#             for j in range(high_j - 1, -1, -1):
#                 ans.append((1 << (i - 1)) + ans[j])
#         return ans

class Solution:
    def grayCode(self, n: int):
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans
