#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/22
'''

from collections import Counter
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        records = Counter(s)
        n = len(s)
        return records[letter] * 100 // n