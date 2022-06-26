#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/13
'''

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min([counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n']])