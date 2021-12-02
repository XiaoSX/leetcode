# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 下午2:39
# @Author  : RenMeng
# @File    : q97_2.py

# 动规
# f(i, j) = f(i-1, j) (if s1[i] == s3[i + j]) or f(i, j - 1)(if s2[j] == s3[i + j])
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][0] = 1

        for i in range(1, n + 1):
            if s2[:i] != s3[:i]:
                break
            f[0][i] = 1

        for i in range(1, m + 1):
            if s1[:i] != s3[:i]:
                break
            f[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = (f[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                            f[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return f[m][n] == 1

