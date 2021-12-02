#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-21
'''

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = set(wordDict)
        split_points = set([0])

        for i in range(1, len(s) + 1):
            for j in split_points:
                if s[j:i] in wordDict:
                    split_points.add(i)
                    break
        return len(s) in split_points