#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/20
'''

from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        if n == 1:
            return True

        if bits[-2] == 0:
            return True

        cnt = 0
        j = n - 2
        while j >= 0 and bits[j] == 1:
            cnt += 1
            j -= 1
        if cnt % 2 == 0:
            return True
        else:
            return False