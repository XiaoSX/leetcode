#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/19
'''

import re

class Solution:
    def __init__(self):
        self.memory = {}

    def doSearch(self, s, p, star_cnt):
        if s == '' and p == '':
            return True

        if s == '':
            return False

        if p == '':
            return False


        if star_cnt == 0 and len(s) != len(p):
            return False


        if (s, p) in self.memory:
            return self.memory[(s, p)]

        sn = len(s)
        pn = len(p)
        si = 0
        pi = 0
        while si < sn and pi < pn:
            if (s[si] == p[pi] or p[pi] == '.') and (pi < pn - 1 and p[pi + 1] != '*' or pi == pn - 1):
                si += 1
                pi += 1
                continue
            if p[pi] == '*':
                target = p[pi - 1]
                if target == '.':
                    for j in range(sn - si + 1):
                        if self.doSearch(s[si+j:], p[pi + 1:], star_cnt - 1):
                            self.memory[(s, p)] = True
                            return self.memory[(s, p)]
                else:
                    for j in range(sn - si + 1):
                        if j == 0:
                            if self.doSearch(s[si + j:], p[pi + 1:], star_cnt - 1):
                                self.memory[(s, p)] = True
                                return self.memory[(s, p)]

                        elif s[si + j - 1] == target and self.doSearch(s[si + j:], p[pi + 1:], star_cnt - 1):
                            self.memory[(s, p)] = True
                            return self.memory[(s, p)]
                        elif s[si + j - 1] != target:
                            self.memory[(s, p)] = False
                            return self.memory[(s, p)]
                self.memory[(s, p)] = False
                return self.memory[(s, p)]
            elif pi < pn - 1 and p[pi + 1] == '*':
                pi += 1
                continue
            self.memory[(s, p)] = False
            return self.memory[(s, p)]

        if si ==  sn and pi == pn:
            self.memory[(s, p)] = True
        elif p[pi:] == '*' or re.search('^([a-z\.]\*){1,}$', p[pi:]):
            self.memory[(s, p)] = True
        else:
            self.memory[(s, p)] = False
        return self.memory[(s, p)]



    def isMatch(self, s: str, p: str) -> bool:
        p2 = ''
        star_cnt = 0
        for i in range(len(p)):
            if i > 0 and p[i - 1] == '*' and p[i] == '*':
                continue

            p2 += p[i]
            if p[i] == '*':
                star_cnt += 1


        return self.doSearch(s, p2, star_cnt)
        # return self.memory[s, p2]