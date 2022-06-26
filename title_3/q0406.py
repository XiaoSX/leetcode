#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/16
'''

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        stack = []
        node = root
        flag = False
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            if flag:
                return node

            if node == p:
                flag = True
            node = node.right

        return None