#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/27
'''

from typing import List
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        dis = n
        w1 = -1
        w2 = -1
        for i in range(n):
            cur_word = words[i]
            if cur_word == word1:
                w1 = i
            if cur_word == word2:
                w2 = i
            if w1 == -1 or w2 == -1:
                continue
            dis = min(dis, abs(w1 - w2))

        return dis


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
    word1 = "a"
    word2 = "student"
    test.append([words, word1, word2])
    ans.append(1)

    words = ["I", "am", "a", "from", "a", "university", "student", "a", "student", "a", "a"]
    word1 = "a"
    word2 = "student"
    test.append([words, word1, word2])
    ans.append(1)
    for i in range(len(test)):
        assert s.findClosest(*test[i]) == ans[i]