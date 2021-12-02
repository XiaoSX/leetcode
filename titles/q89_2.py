# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 上午11:39
# @Author  : RenMeng
# @File    : q89_2.py


class Solution:
    def grayCode(self, n: int):
        ans = []
        for i in range(1 << n):
            ans.append(i ^ (i >> 1))
        return ans