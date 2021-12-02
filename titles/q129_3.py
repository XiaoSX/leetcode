#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-17
'''
from titles.tree import TreeNode
class Solution:
    def getSum(self, root, total):
        if root is None:
            return 0
        cur_v = total * 10 + root.val
        if root.left is None and root.right is None:
            return cur_v

        return self.getSum(root.left, cur_v) + self.getSum(root.right, cur_v)

    def sumNumbers(self, root: TreeNode) -> int:
        return self.getSum(root, 0)