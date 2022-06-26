#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/6
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = -1
        s_dict = {}
        max_len = 0
        for i in range(n):
            if s[i] in s_dict and s_dict[s[i]] >= left:
                left = s_dict[s[i]]
            s_dict[s[i]] = i
            max_len = max(max_len, i - left)

        return max_len


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append("abcabcbb")
    ans.append(3)

    test.append("bbbbb")
    ans.append(1)

    test.append("pwwkew")
    ans.append(3)

    test.append(' ')
    ans.append(1)

    test.append("abba")
    ans.append(2)

    for i in range(len(test)):
        assert  s.lengthOfLongestSubstring(test[i]) == ans[i]
