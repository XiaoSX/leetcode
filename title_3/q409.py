#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/2
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        f = [[0 for _ in range(n)] for _ in range(n)]
        max_len = 0
        ans = ''
        for i in range(n):
            f[i][i] = 1
            max_len = 1
            if max_len > len(ans):
                ans = s[i:i+1]
            if i + 1 < n and s[i] == s[i + 1]:
                f[i][i + 1] = 2
                max_len = max(max_len, f[i][i + 1])
                if max_len > len(ans):
                    ans = s[i:i + 2]

        for i in range(2, n):
            for j in range(n - i):
                if s[j] == s[j + i] and f[j + 1][j + i - 1] > 0:
                    f[j][j + i] = f[j + 1][j + i - 1] + 2
                    max_len = max(max_len, f[j][j + i])
                    if max_len > len(ans):
                        ans = s[j:j + i + 1]



        return ans


if __name__ == '__main__':
    s = Solution()
    t = "abccccdd"
    ans = s.longestPalindrome(t)
    assert ans == 7
