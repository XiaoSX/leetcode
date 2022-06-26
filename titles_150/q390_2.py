#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/2
'''
class Solution:
    def __init__(self):
        self.flag = True

    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return n
        if n % 2 != 0:
            self.flag = not self.flag
            return 2 * self.lastRemaining(n // 2)
        if not self.flag:
            self.flag = not self.flag
            return 2 * self.lastRemaining(n // 2) - 1
        self.flag = not self.flag
        return 2 * self.lastRemaining(n // 2)