#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/4
'''
# 美好串的子串不一定是美好串
class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        last_point = 0
        n = len(s)
        result = ''
        while last_point < n:
            seen = set()
            state = set()
            pre_p = last_point
            # 以当前字母开头的子串是否是美好的
            for i in range(pre_p, n):
                if s[i] not in seen:
                    seen.add(s[i])
                state.add(s[i])
                if s[i].capitalize() in seen and s[i].lower() in seen:
                    if s[i].capitalize() in state:
                        state.remove(s[i].capitalize())
                    if s[i].lower() in state:
                        state.remove(s[i].lower())
                    if len(state) == 0:
                        last_point = i
            last_point += 1
            if len(s[pre_p:last_point]) > 1 and len(result) < len(s[pre_p:last_point]):
                result = s[pre_p:last_point]
        return result


