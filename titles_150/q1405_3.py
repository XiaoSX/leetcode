#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/7
'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                hasNext = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ans)