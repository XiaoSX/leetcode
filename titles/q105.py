#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-26
'''
from titles.tree import TreeNode
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        ri = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:ri + 1], inorder[:ri])
        root.right = self.buildTree(preorder[ri+1:], inorder[ri + 1:])
        return root
