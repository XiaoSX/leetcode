#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/2
'''

class Solution:
    def lastRemaining(self, n: int) -> int:
        return 1 if n == 1 else 2 * (n // 2 + 1 - self.lastRemaining(n // 2))