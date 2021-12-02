# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 上午11:14
# @Author  : RenMeng
# @File    : q58.py


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and cnt == 0:
                continue
            if s[i] == ' ':
                return cnt
            else:
                cnt += 1
        return cnt