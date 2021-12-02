#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-29
'''


class Solution:
    def wordBreak(self, s: str, wordDict):
        def breakwords(index, s):
            if index == len(s):
                return [[]]

            ans = []
            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordDict:
                    nextbreak = breakwords(i, s)
                    for sen in nextbreak:
                        ans.append(sen[:] + [s[index:i]])
            return ans

        wordDict = set(wordDict)
        ans = breakwords(0, s)
        return [' '.join(x[::-1]) for x in ans]
