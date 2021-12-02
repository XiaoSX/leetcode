#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-17
'''
from titles.tree import TreeNode
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        ans = 0
        if root.left is not None:
            root.left.val += root.val * 10
            ans += self.sumNumbers(root.left)
        if root.right is not None:
            root.right.val += root.val * 10
            ans += self.sumNumbers(root.right)
        return ans