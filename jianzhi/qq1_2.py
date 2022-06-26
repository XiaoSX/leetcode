#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/22
'''

def divide(self, a: int, b: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if a == INT_MIN and b == -1:
        return INT_MAX

    ans = 0

    # 处理边界，防止转正数溢出
    if b == INT_MIN:  # 除数绝对值最大，结果必为 0 或 1
        return 1 if a == b else 0
    if a == INT_MIN:  # 被除数先减去一个除数
        a -= -abs(b)
        ans += 1

    sign = -1 if (a > 0) ^ (b > 0) else 1

    a, b = abs(a), abs(b)
    for i in range(31, -1, -1):
        if (a >> i) - b >= 0:
            a = a - (b << i)
            # 代码优化：这里控制 ans 大于等于 INT_MAX
            if ans > INT_MAX - (1 << i):
                return INT_MIN
            ans += 1 << i
    # bug 修复：因为不能使用乘号，所以将乘号换成三目运算符
    return ans if sign == 1 else -ans