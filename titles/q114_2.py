#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-24
'''

from titles.tree import TreeNode
# 收集右子树并入栈
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stacks = []
        node = root
        while node:
            while node.left:
                if node.right:
                    stacks.append(node.right)
                node.right = node.left
                node.left = None
                node = node.right
            if node.right is None and len(stacks) > 0:
                next_node = stacks.pop(-1)
                node.right = next_node
            node = node.right
