#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/23
'''

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        refers = {}
        count = {}
        n = len(s)
        m = len(words[0])
        cnt = len(words)

        i = 0
        for word in words:
            if word not in refers:
                refers[word] = i
                i += 1
                count[word] = 0
            count[word] += 1
        ans = []

        for i in range(n - m * cnt + 1):
            split_words = s[i: i + m * cnt]
            visit = [0 for _ in range(len(refers))]
            for j in range(0, m * cnt, m):
                cur = split_words[j:j+m]
                if cur in refers:
                    visit[refers[cur]] += 1
                    if visit[refers[cur]] > count[cur]:
                        break
                else:
                    break
            else:
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    t = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    ans = s.findSubstring(t, words)
    print(ans)