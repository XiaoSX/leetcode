#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-17
'''
from collections import defaultdict
from copy import deepcopy
class Solution:
    def compare(self, a, b):
        m = len(a)
        n = len(b)
        c = a + b
        d = b + a
        for i in range(m + n):
            if int(c[i]) > int(d[i]):
                return 1
            if int(c[i]) < int(d[i]):
                return -1
        return 0

    def prefix(self, text):
        n = len(text)
        for j in range(1, n):
            for i in range(n-j):
                d = self.compare(text[i], text[i+1])
                if d == -1:
                    text[i], text[i+1] = text[i+1], text[i]
        return ''.join(text)


    def subNumber(self, text, prefix, text_len):
        i = len(prefix)
        dict_info = defaultdict(lambda : 0)
        n = len(text)
        for j in range(n):
            if i < len(text[j]):
                cur_str = text[j][i]
            else:
                cur_str = prefix[0]
            dict_info[cur_str] += 1
        for j in range(8, -1, -1):
            dict_info[str(j)] += dict_info[str(j+1)]
        new_arr = ['' for _ in range(text_len)]
        new_dict_info = deepcopy(dict_info)
        for j in range(n-1, -1, -1):
            if i < len(text[j]):
                cur_str = text[j][i]
            else:
                cur_str = prefix[0]
            new_arr[dict_info[cur_str] - 1] = text[j]
            dict_info[cur_str] -= 1
        total_str = ''
        dict_info = new_dict_info
        pre_v = 0
        for j in range(9, -1, -1):
            cnt = dict_info[str(j)] - pre_v
            pre_v = dict_info[str(j)]
            if cnt == 0:
                continue
            if cnt == 1:
                total_str += new_arr[dict_info[str(j)] - 1]
            elif cnt > 1:
                new_text = new_arr[dict_info[str(j+1)]: dict_info[str(j)]]
                if len(new_text) == text_len:
                    total_str += self.prefix(new_text)
                else:
                    total_str += self.subNumber(new_text, prefix + str(j), len(new_text))
        return total_str



    def largestNumber(self, nums) -> str:
        # O(n)的空间复杂度
        nums_str = []
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            nums_str.append(str(cur))
        total_str= self.subNumber(nums_str, '', n)
        n = len(total_str) - 1
        start = 0
        for i in range(n):
            if total_str[i] == '0':
                start += 1
            else:
                break
        return total_str[start:]


