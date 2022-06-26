#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/24
'''

class Solution:
    def strToInt(self, strings) -> int:
        max_v = (1 << 31) - 1
        sign = 0
        ans = 0
        for t in strings:
            # int parse, will break when the condition are wrong
            # 数字部分的退出条件, 'sign == 0 时遇到 +/-/space'
            if t in ['+', '-'] + [str(i) for i in range(10)]:
                if t == '+' and sign == 0:
                    sign = 1
                elif t == '-' and sign == 0:
                    sign = -1
                elif t in '0123456789':
                    if sign == 0:
                        sign = 1
                    ans = ans * 10 + int(t)
                    if ans >= (1 << 31):
                        ans = 1 << 31
                        break
                else:
                    break
            # skip space
            elif t.isspace() and sign == 0:
                continue
            # condition wrong, break directly
            else:
                break

        if sign == -1:
            return sign * ans
        return min(max_v, ans)