#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-22
'''
from collections import defaultdict
class Solution:

    def findRepeatedDnaSequences(self, s):
        N = 100000
        P = 131313
        h = [0 for _ in range(N)]
        p = [0 for _ in range(N)]

        n = len(s)
        ans = set()
        p[0] = 1
        for i in range(1, n+1):
            h[i] = h[i - 1] * P + s[i - 1]
            p[i] = p[i - 1] * P

        map = defaultdict(lambda :0)
        for i in range(1, n - 10 + 2):
            j = i + 10 - 1
            hash = h[j] - h[i - 1] * p[j - i + 1]
            cnt = map[hash]
            if (cnt == 1):
                ans.add(s.substring(i - 1, i + 10 - 1))
            map[hash] = cnt + 1
        return ans

