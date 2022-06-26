#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-08
'''
# 负数问题
# 整数，小数分开处理，整数前导0和都是0的情况
# 除数按位保存
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        nums = []
        flag = 0
        if numerator < 0:
            numerator = abs(numerator)
            if denominator < 0:
                denominator = abs(denominator)
            elif denominator > 0:
                flag = 1
        elif numerator > 0:
            if denominator < 0:
                denominator = abs(denominator)
                flag = 1


        # 负数情况
        while numerator != 0:
            nums.append(numerator % 10)
            numerator = numerator // 10

        nums = nums[::-1]
        ans = []
        remain = 0
        for i in range(len(nums)):
            de_num = remain * 10 + nums[i]
            shang = de_num // denominator
            remain = de_num % denominator
            ans.append(shang)

        # 前导0和都是0的情况
        i = 0
        while i < len(ans) and ans[i] == 0:
            i += 1
        ans = ans[i:]
        if len(ans) == 0:
            ans = [0]

        if remain != 0:
            ans.append('.')
            location = {}
            while remain != 0 and remain * 10 not in location:
                de_num = remain * 10
                shang = de_num // denominator
                remain = de_num % denominator
                location[de_num] = len(ans)
                ans.append(shang)
            if remain != 0:
                j = location[remain * 10]
                ans.append(' ')
                for i in range(len(ans) - 2, j - 1, -1):
                    ans[i + 1] = ans[i]
                ans[j] = '('
                ans.append(')')
        if flag == 1:
            ans = ['-'] + ans
        return ''.join([str(x) for x in ans])
