# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 上午10:22
# @Author  : RenMeng
# @File    : q89.py

class Solution:
    def grayCode(self, n: int):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        ans = [0, 1, 3, 2]
        for i in range(2, n):
            size = len(ans)
            for j in range(size - 1, -1, -1):
                ans.append(ans[j] + size)
        return ans