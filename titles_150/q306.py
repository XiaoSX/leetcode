#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/10
'''

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            if int(num[:i+1]) == 0 or num[0] != '0':
                dp[0][i] = 1
            if i >= 1 and (int(num[1:i+1]) == 0 or num[1] != '0'):
                dp[1][i] = 1


        for l in range(n):
            for i in range(2, n-l):
                if num[i] == '0' and l >= 1 and int(num[i:i+l+1]) != 0:
                    continue
                for p in range(max(1, i-l-1), i):
                    for q in range(max(0, p-l-1), p):
                        if q == 0 and int(num[i:i+l+1]) == int(num[q:p]) + int(num[p:i]):
                            if num[p] == '0' and int(num[p:i]) != 0:
                                continue
                            if num[q] == '0' and int(num[q:p]) != 0:
                                continue
                            dp[i][i+l] = 1
                            dp[q][p-1] = 1
                            dp[p][i-1] = 1
                        elif q != 0:
                            if dp[q][p-1] and dp[p][i-1] and int(num[i:i+l+1]) == int(num[q:p]) + int(num[p:i]):
                                dp[i][i+l] = 1

                        if dp[i][i+l] == 1:
                            break
                    if dp[i][i + l] == 1:
                        break
                if i + l == n - 1 and dp[i][i + l] == 1:
                    return True

        return False