#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/12
'''


from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if len(word) != len(pattern):
                continue

            pattern_p = {}
            word_p = {}
            i = 0
            n = len(word)
            while i < n:
                f = word[i]
                t = pattern[i]
                if f not in word_p and t not in pattern_p:
                    word_p[f] = i
                    pattern_p[t] = i
                elif f in word_p and t in pattern_p and word_p[f] == pattern_p[t]:
                    pass
                else:
                    break

                i += 1

            if i == n:
                ans.append(word)

        return ans


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    words = ["a", "b", "c"]
    pattern = "a"
    test.append([words, pattern])
    ans.append(["a", "b", "c"])

    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    test.append([words, pattern])
    ans.append(["mee", "aqq"])

    for i in range(len(test)):
        assert s.findAndReplacePattern(*test[i]) == ans[i]