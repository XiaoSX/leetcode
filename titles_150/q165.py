#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-08
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = version1.split('.')
        num2 = version2.split('.')
        m = len(num1)
        n = len(num2)
        if m > n:
            num2 += [0 for _ in range(m - n)]
        else:
            num1 += [0 for _ in range(n - m)]
        for i in range(max(m, n)):
            if int(num1[i]) > int(num2[i]):
                return 1
            elif int(num1[i]) < int(num2[i]):
                return -1
        return 0