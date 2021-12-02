#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-21
'''
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        split_points = defaultdict(list)

        for i in range(1, len(s) + 1):
            children = list(split_points.keys())

            if s[:i] in wordDict:
                split_points[i].append([s[:i]])

            for j in children:
                if s[j:i] in wordDict:
                    for ws in split_points[j]:
                        split_points[i].append(ws + [s[j:i]])

        if len(s) in split_points:
            return [' '.join(x) for x in split_points[len(s)]]
        return []
