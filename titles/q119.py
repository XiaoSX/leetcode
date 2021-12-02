#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-27
'''

class Solution:
    def getRow(self, rowIndex: int):
        ans = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            ans[i] = int(ans[i - 1] * (rowIndex - i + 1) / i)
        return ans