#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/2
'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        counter = Counter(s)
        single = 0
        ans = 0
        for key in counter:
            if counter[key] % 2 == 0:
                ans += counter[key]
            else:
                ans += counter[key] - 1
                single = 1

        ans += single
        return ans

if __name__ == '__main__':
    s = Solution()
    t = "ab"
    ans = s.longestPalindrome(t)
    assert ans == 1