# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午2:34
# @Author  : RenMeng
# @File    : q94.py

from titles.tree import TreeNode
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)