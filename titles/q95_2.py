# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午2:00
# @Author  : RenMeng
# @File    : q95_2.py

from titles.tree import TreeNode
class Solution:
    def createTree(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            for left_t in self.createTree(start, i - 1):
                for right_t in self.createTree(i + 1, end):
                    # list 中每次都append一个新对象
                    tree = TreeNode()
                    tree.val = i
                    tree.left = left_t
                    tree.right = right_t
                    all_trees.append(tree)
        return all_trees


    def generateTrees(self, n: int):
        return self.createTree(1, n)