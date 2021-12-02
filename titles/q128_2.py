#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-10
'''
class Solution:
    def __init__(self):
        self.a = {}

    def find(self, x):
        if x in self.a:
            self.a[x] = self.find(self.a[x])
            return self.a[x]
        else:
            return x

    def longestConsecutive(self, nums) -> int:
        for x in nums:
            self.a[x] = x + 1

        ans = 0
        for x in nums:
            y = self.find(x + 1)
            ans=max(ans,y-x)

        return ans