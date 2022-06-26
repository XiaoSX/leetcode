#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/28
'''

from typing import List

import numpy as np
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        arr = np.arange(n)
        a = sorted(arr, key=lambda x: properties[x][0], reverse=True)
        b = sorted(arr, key=lambda x: properties[x][1], reverse=True)

        week = set()
        i = 0
        j = n - 1
        while j >= 0 and i < n:
            if a[i] in week:
                i += 1
                continue

            attack = properties[a[i]][0]
            defense = properties[a[i]][1]
            while j >= 0 and properties[b[j]][1] < defense:
                if properties[b[j]][0] < attack:
                    week.add(b[j])
                j -= 1
            i += 1
        return len(week)


