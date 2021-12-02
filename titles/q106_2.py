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
        stack = [root]
        n = len(postorder)
        inorderIndex = n - 1
        for i in range(n - 2, -1, -1):
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.right = TreeNode(postorder[i])
                stack.append(node.right)
            else:
                while len(stack) > 0 and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop(-1)
                    inorderIndex -= 1
                node.left = TreeNode(postorder[i])
                stack.append(node.left)
        return root