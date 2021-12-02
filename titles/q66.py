# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 上午11:21
# @Author  : RenMeng
# @File    : q66.py


class Solution:
    def plusOne(self, digits):
        pre_v = (digits[-1] + 1) // 10
        digits[-1] = int((digits[-1] + 1) % 10)
        for i in range(len(digits) - 2, -1, -1):
            if pre_v == 0:
                return digits

            v = (pre_v + digits[i]) // 10
            digits[i] = int((pre_v + digits[i]) % 10)
            pre_v = v

        if pre_v != 0:
            digits.insert(0, pre_v)
        return digits