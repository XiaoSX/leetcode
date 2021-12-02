#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-10-30
'''


from math import floor, ceil
class Solution:
    # int(tokens)
    def generate_num(self, tokens):
        if not isinstance(tokens, str):
            return tokens
        sign = True if tokens[0] == '-' else False
        tokens = tokens[1:] if sign else tokens
        number = 0
        b = 1
        for i in range(len(tokens)-1, -1, -1):
            number += int(tokens[i]) * b
            b *= 10
        number = -number if sign else number
        return number

    # 利用字典，返回一个函数对象
    def get_answer(self, a, b, s):
        a = self.generate_num(a)
        b = self.generate_num(b)
        if s == '+':
            return a + b
        if s == '-':
            return a - b
        if s == '*':
            return a * b
        if s == '/':
            c = a / b
            if c < 0:
                return ceil(a / b)
            else:
                return floor(a / b)

    def evalRPN(self, tokens) -> int:
        stacks = []
        for s in tokens:
            if s in ['+', '-', '*', '/']:
                b = stacks.pop(-1)
                a = stacks.pop(-1)
                stacks.append(self.get_answer(a, b, s))
            else:
                stacks.append(s)
        return self.generate_num(stacks[0])