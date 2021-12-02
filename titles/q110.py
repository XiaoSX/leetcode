#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-15
'''

from titles.tree import TreeNode
class Solution:
    def sub_isBalanced(self, root):
        if root is None:
            return True, 0
        left_bool, left_height = self.sub_isBalanced(root.left)
        if not left_bool:
            return False, 0
        right_bool, right_height = self.sub_isBalanced(root.right)
        if not right_bool:
            return False, 0
        if abs(left_height - right_height) <= 1:
            return True, max(left_height, right_height) + 1
        return False, 0

    def isBalanced(self, root: TreeNode) -> bool:
        root_bool, _ = self.sub_isBalanced(root)
        return root_bool


