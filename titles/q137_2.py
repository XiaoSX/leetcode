#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

# python 对“有符号整数类型”和“无符号整数类型”不区分
# 位运算，取第i位，(num >> i) & 1
# 位运算，赋值第i位， ans |= (1 << i), 不需要用字符串收集
# 最高符号位， 补码=2^(32) - 真值；所以当最高位是1的时候，代表该真值为负，答案=真值-2^(32)
class Solution:
    def singleNumber(self, nums) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


    # def singleNumber(self, nums) -> int:
    #     ans = ''
    #     for i in range(32):
    #         sum = 0
    #         for n in nums:
    #             a = int(format(n, '032b')[i])
    #             sum += a
    #         ans += str(sum % 3)
    #     return int(ans, 2)