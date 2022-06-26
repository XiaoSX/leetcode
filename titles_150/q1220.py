#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/17
'''

# 大量重复计算
# 以a, e, i, o, u 结尾的字符串个数，形成子结构
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a_cnt = 1
        e_cnt = 1
        i_cnt = 1
        o_cnt = 1
        u_cnt = 1
        mod = 1e9 + 7
        for i in range(2, n + 1):
            na_cnt = (e_cnt + i_cnt + u_cnt) % mod
            ne_cnt = (a_cnt + i_cnt) % mod
            ni_cnt = (e_cnt + o_cnt) % mod
            no_cnt = i_cnt % mod
            nu_cnt = (o_cnt + i_cnt) % mod
            a_cnt, e_cnt, i_cnt, o_cnt, u_cnt = na_cnt, ne_cnt, ni_cnt, no_cnt, nu_cnt

        ans = 0
        for num in [a_cnt ,e_cnt, i_cnt, o_cnt, u_cnt]:
            ans += num
            if ans >= mod:
                ans %= mod
        return int(ans)