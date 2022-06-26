#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/28
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        cnt = 0
        while n > 0 or cnt < 32:
            b = n % 2
            ans = (ans << 1) + b
            n = n // 2
            cnt += 1
        return ans