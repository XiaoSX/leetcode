#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/19
'''

from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        maxDef = 0
        for _, def_ in properties:
            if maxDef > def_:
                ans += 1
            else:
                maxDef = max(maxDef, def_)
        return ans