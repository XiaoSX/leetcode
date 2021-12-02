# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 下午3:45
# @Author  : RenMeng
# @File    : q87.py

# s2 from s1, 必然存在切分点, 使得左右子树对应相等, 递归
# 解空间和直接判断
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dps = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dps[i][j][0] = True
                else:
                    dps[i][j][0] = False


        for step in range(1, n):
            for i in range(n - step):
                for j in range(n - step):
                    for k in range(step):
                        left_tree = dps[i][j][k]
                        right_tree = dps[i+k+1][j+k+1][step-k-1]
                        if left_tree and right_tree:
                            dps[i][j][step] = True
                            break

                        left_tree = dps[i][j + step - k][k]
                        right_tree = dps[i + k + 1][j][step - k - 1]
                        if left_tree and right_tree:
                            dps[i][j][step] = True
                            break
        return dps[0][0][n-1]


# class Solution:
#     def isScramble(self, s1: str, s2: str) -> bool:
#         if len(s1) != len(s2):
#             return False
#         if s1 == s2:
#             return True
#         if sorted(s1) != sorted(s2):
#             return False
#
#         for i in range(1, len(s1)):
#             if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
#                     (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
#                 return True
#         return False


