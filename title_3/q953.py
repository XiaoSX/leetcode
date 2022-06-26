#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/17
'''

from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(order)
        m = len(words)
        if m == 0:
            return True

        i = 0
        j = 0
        while i < n and j < m:
            if order[i] != words[j][0]:
                i += 1
                continue

            tmp = []
            while j < m and order[i] == words[j][0]:
                if len(tmp) > 0 and len(words[j]) == 1:
                    return False
                if len(words[j]) > 1:
                    tmp.append(words[j][1:])
                j += 1
            if len(tmp) > 1:
                if not self.isAlienSorted(tmp, order):
                    return False

        if j >= m:
            return True

        if i >= n:
            return False


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    test.append([words, order])
    ans.append(True)

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    test.append([words, order])

    ans.append(False)

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    test.append([words, order])

    ans.append(False)

    for i in range(len(test)):
        assert s.isAlienSorted(*test[i]) == ans[i]


