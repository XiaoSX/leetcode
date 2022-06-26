#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/21
'''

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def doFlatten(token, left_cnt, right_cnt, cnt):
            # 用完
            if left_cnt == cnt and right_cnt == cnt:
                ans.append(token)
                return

            # 左括号用完
            if left_cnt == cnt:
                doFlatten(token + ')', left_cnt, right_cnt + 1, cnt)
            # 初始
            elif left_cnt == right_cnt:
                doFlatten(token + '(', left_cnt + 1, right_cnt, cnt)
            else:
                doFlatten(token + '(', left_cnt + 1, right_cnt, cnt)
                doFlatten(token + ')', left_cnt, right_cnt + 1, cnt)

        doFlatten('', 0, 0, n)
        return ans