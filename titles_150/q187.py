#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-22
'''
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        s_dict = defaultdict(lambda :0)
        ans = []
        n = len(s)
        target_len = 10
        for i in range(n-target_len+1):
            s_dict[s[i:i+target_len]] += 1
        for text in s_dict:
            if s_dict[text] > 1:
                ans.append(text)
        return ans

