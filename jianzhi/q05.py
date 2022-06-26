#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/8
'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        new_s = ''
        for t in s:
            if t == ' ':
                new_s += '%20'
            else:
                new_s += t
        return new_s