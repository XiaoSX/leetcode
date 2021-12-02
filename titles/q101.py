#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-01
'''

from titles.tree import TreeNode
class Solution:
    def subSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        cond1 = self.subSymmetric(left.left, right.right)
        cond2 = self.subSymmetric(left.right, right.left)
        if cond1 and cond2:
            return True
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.subSymmetric(root.left, root.right)