#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-15
'''
from titles.tree import TreeNode
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#
#         left_h = self.maxDepth(root.left)
#         right_h = self.maxDepth(root.right)
#         return max(left_h, right_h) + 1
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#
#         node = root
#         stacks = []
#         heis = []
#         max_height = 0
#         height = 0
#         while len(stacks) > 0 or node is not None:
#             while node:
#                 height += 1
#                 stacks.append(node)
#                 heis.append(height)
#                 node = node.left
#             node = stacks.pop(-1)
#             height = heis.pop(-1)
#             node = node.right
#             if node is None:
#                 max_height = max(max_height, height)
#         return max_height

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        node = root
        queues = [node]
        max_height = 0
        while len(queues) > 0:
            qs = len(queues)
            while qs > 0:
                node = queues.pop(0)
                if node.left:
                    queues.append(node.left)
                if node.right:
                    queues.append(node.right)
                qs -= 1
            max_height += 1
        return max_height
