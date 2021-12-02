#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-24
'''

from titles.tree import TreeNode
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        node = root
        stacks = []
        # 先序遍历
        while node or len(stacks) > 0:
            stacks.append(node)  # 先根
            while node.left is not None:
                stacks.append(node.left)  # 先根
                node = node.left
            parent = stacks.pop(-1)
            while parent.right is None and len(stacks) > 0:
                parent = stacks.pop(-1)
            node.left = parent.right
            node = parent.right

        node = root
        while node.left is not None or node.right is not None:
            if node.left is not None:
                node.right = node.left
                next_node = node.left
                node.left = None
                node = next_node
