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
        if len(tokens) == 1:
            return self.generate_num(tokens[0])

        new_tokens = [tokens[0], tokens[1]]
        for i in range(2, len(tokens)):
            a = tokens[i - 2]
            b = tokens[i - 1]
            c = tokens[i]
            d = ['+', '-', '*', '/']
            if (c in d) and (a not in d) and (b not in d):
                new_tokens.pop(-1)
                new_tokens.pop(-1)
                new_tokens.append(self.get_answer(a, b, c))
            else:
                new_tokens.append(c)
        return self.evalRPN(new_tokens)
