#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-26
'''
from titles.tree import TreeNode
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        ri = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:ri], postorder[:ri])
        root.right = self.buildTree(inorder[ri + 1:], postorder[ri:-1])
        return root