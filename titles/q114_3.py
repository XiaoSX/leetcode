#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-24
'''

from titles.tree import TreeNode
# 将右子树挂到左子树最右结点[根左右]
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        node = root
        while node:
            if node.left is None:
                node = node.right
            else:
                pre_node = node.left
                while pre_node.right:
                    pre_node = pre_node.right
                pre_node.right = node.right
                node.right = node.left
                node.left = None
                node = node.right