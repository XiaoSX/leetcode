# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 上午10:30
# @Author  : RenMeng
# @File    : q97.py

# 递归搜索逻辑:
#   子问题1是True, 则return
#       else: 搜索下一个子问题, 是True, 则return
#       else: 搜索下一个子问题
# Note: 不能直接返回子问题的结果, 递归解!=子问题解
# 存储的时候, 用下标可以用多维数组, 不然就要构造key
class Solution:
    def __init__(self):
        self.dict = {}

    def assign_key(self, s1, s2, s3, v):
        key = '-'.join([s1, s2, s3])
        self.dict[key] = v
        key = '-'.join([s2, s1, s3])
        self.dict[key] = v


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        key = '-'.join([s1, s2, s3])
        if key in self.dict:
            return self.dict[key]

        key = '-'.join([s2, s1, s3])
        if key in self.dict:
            return self.dict[key]
        if s1 == '' and s2 == '' and s3 == '':
            self.assign_key(s1, s2, s3, True)
            return True

        if s1 == '' and s2 == '' and s3 != '':
            self.assign_key(s1, s2, s3, False)
            return False

        if s3 == '':
            self.assign_key(s1, s2, s3, False)
            return False

        if s1 == '':
            if s2 == s3:
                self.assign_key(s1, s2, s3, True)
                return True
            else:
                self.assign_key(s1, s2, s3, False)
                return False

        if s2 == '':
            if s1 == s3:
                self.assign_key(s1, s2, s3, True)
                return True
            else:
                self.assign_key(s1, s2, s3, False)
                return False

        if len(s1) + len(s2) != len(s3):
            self.assign_key(s1, s2, s3, False)
            return False

        if s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]):
            self.assign_key(s1, s2, s3, True)
            return True
        elif s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]):
            self.assign_key(s1, s2, s3, True)
            return True
        self.assign_key(s1, s2, s3, False)
        return False
