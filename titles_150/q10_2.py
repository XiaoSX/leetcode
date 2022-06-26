#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/20
'''

import re

"""
# 不是结束条件: s=='' p!=''
# 结束条件: s!='' p==''

"""
class Solution:
    def __init__(self):
        self.memory = {}

    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True

        if s == '' and p == '':
            return True

        if s != '' and p == '':
            return False

        if (s, p) in self.memory:
            return self.memory[(s, p)]

        p = re.sub('\*{2,}', '*', p)
        sn = len(s)
        pn = len(p)
        si = 0
        pi = 0
        while pi < pn:
            # 搜索
            if pi < pn - 1 and p[pi + 1] == '*':
                target = p[pi]
                if si == sn:
                    match = self.isMatch('', p[pi+2:])
                    self.memory[(s, p)] = match
                    return match
                else:
                    j = 0
                    while 1:
                        # s搜索完, 退出
                        if j == sn - si + 1:
                            match = self.isMatch('', p[pi + 2:])
                            self.memory[(s, p)] = match
                            return match

                        # 所有搜索空间都不匹配, 退出
                        if j > 0 and target != '.' and s[si+j-1] != target:
                            self.memory[(s, p)] = False
                            return False

                        # 只要有true, 就为true, 否则, 搜索所有
                        match = self.isMatch(s[si+j:], p[pi+2:])
                        if match:
                            self.memory[(s, p)] = match
                            return match

                        j += 1

            else:
                if si == sn:
                    self.memory[(s, p)] = False
                    return False

                if s[si] == p[pi] or p[pi] == '.':
                    si += 1
                    pi += 1
                else:
                    self.memory[(s, p)] = False
                    return False

        if si == sn:
            self.memory[(s, p)] = True
            return True
        else:
            self.memory[(s, p)] = False
            return False