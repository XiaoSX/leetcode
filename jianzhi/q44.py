#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/25
'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        base_num = 1
        total_nums = 9
        num_cnt = 1
        ans = total_nums * num_cnt

        while n > ans:
            n -= ans
            num_cnt += 1
            total_nums *= 10
            ans = num_cnt * total_nums
            base_num *= 10

        # 当前基数
        cur_num = n // num_cnt + base_num
        ith = n % num_cnt - 1
        if ith == -1:
            return (cur_num - 1) % 10
        else:
            return int(str(cur_num)[ith])