#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/19
'''

from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        left = [2 * n for _ in range(n)]
        right = [2 * n for _ in range(n)]
        d = 2 * n
        for i in range(n):
            if s[i] == c:
                d = i
            left[i] = d

        d = 2 * n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                d = i
            right[i] = d

        ans = [-1 for _ in range(n)]
        for i in range(n):
            ans[i] = min(abs(i - left[i]), abs(i - right[i]))

        return ans

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    t = "loveleetcode"
    c = "e"
    test.append([t, c])
    ans.append([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
    t = "aaab"
    c = "b"
    test.append([t, c])
    ans.append([3, 2, 1, 0])
    for i in range(len(test)):
        assert s.shortestToChar(*test[i]) == ans[i]

