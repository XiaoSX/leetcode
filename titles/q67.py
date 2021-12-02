# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 上午11:37
# @Author  : RenMeng
# @File    : q67.py

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]