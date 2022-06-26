#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/25
'''


def get_real_and_unreal(num):
    real = 0
    unreal = 0
    if len(num) == 0:
        return real, unreal

    n = len(num)
    unreal_h = n
    unreal_l = n
    # 存在虚部
    if num[n-1] == 'i':
        unreal_h = n - 1
        unreal_l = 0

        i = n - 1
        while i >= 0:
            if num[i] == '-' or num[i] == '+':
                unreal_l = i
                break
            i -= 1

        if unreal_l < unreal_h:
            unreal = int(num[unreal_l:unreal_h])
    if 0 < unreal_l < n and num[unreal_l - 1] in ['+', '-']:
        unreal_l -= 1
    if unreal_l > 0:
        real = int(num[:unreal_l])
    return real, unreal

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, unreal1 = get_real_and_unreal(num1)
        real2, unreal2 = get_real_and_unreal(num2)
        real_ans = real1 * real2 - unreal1 * unreal2
        unreal_ans = real1 * unreal2 + real2 * unreal1
        return str(real_ans) + '+' + str(unreal_ans) + 'i'

