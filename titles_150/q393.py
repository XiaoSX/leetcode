#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/13
'''

from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        ans = False
        n = len(data)
        i = 0
        while i < n:
            cur = data[i]
            if cur & int('10000000', 2) == int('00000000', 2):
                i += 1
            elif cur & int('11100000', 2) == int('11000000', 2):
                for j in range(i + 1, i + 2):
                    if j >= n:
                        return ans

                    if data[j] & int('11000000', 2) == int('10000000', 2):
                        continue
                    else:
                        return ans
                i += 2
            elif cur & int('11110000', 2) == int('11100000', 2):
                for j in range(i + 1, i + 3):
                    if j >= n:
                        return ans

                    if data[j] & int('11000000', 2) == int('10000000', 2):
                        continue
                    else:
                        return ans
                i += 3
            elif cur & int('11111000', 2) == int('11110000', 2):
                for j in range(i + 1, i + 4):
                    if j >= n:
                        return ans

                    if data[j] & int('11000000', 2) == int('10000000', 2):
                        continue
                    else:
                        return ans
                i += 4
            else:
                return ans

        return True