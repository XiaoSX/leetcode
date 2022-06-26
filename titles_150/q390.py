#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/2
'''
class Solution:
    def lastRemaining(self, n: int) -> int:
        flag = True
        ans = []
        while n != 1:
            if n % 2 != 0:
                ans.append([2, 0])
            elif not flag:
                ans.append([2, -1])
            else:
                ans.append([2, 0])
            n = n // 2
            flag = not flag

        output = 1
        for i in range(len(ans) - 1, -1, -1):
            output *= ans[i][0]
            output += ans[i][1]
        return output