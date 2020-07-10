#  -*-  coding: utf-8  -*-
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        records = defaultdict(lambda: -1)
        start = 0
        cur_len = 0
        for i in range(len(s)):
            # 记录字符出现的index
            if s[i] not in records:
                records[s[i]] = i
                continue

            if records[s[i]] == -1:
                records[s[i]] = i
                continue

            # 第二次出现
            now_len = i - start
            cur_len = max(cur_len, now_len)
            new_start = records[s[i]] + 1
            for j in range(start, new_start):
                records[s[j]] = -1
            start = new_start
            records[s[i]] = i
        cur_len = max(cur_len, len(s) - start)
        return cur_len
