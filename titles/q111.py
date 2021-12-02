#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-15
'''

# digui
# guagnsou
# bianli
from titles.tree import TreeNode
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         left_height = self.minDepth(root.left)
#         right_height = self.minDepth(root.right)
#         if left_height == 0:
#             return right_height + 1
#         if right_height == 0:
#             return left_height + 1
#         return min(left_height, right_height) + 1

# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         queues = [root]
#         height = 0
#         while len(queues) > 0:
#             qs = len(queues)
#             while qs > 0:
#                 node = queues.pop(0)
#                 if node.left is None and node.right is None:
#                     return height + 1
#                 if node.left is not None:
#                     queues.append(node.left)
#                 if node.right is not None:
#                     queues.append(node.right)
#                 qs -= 1
#             height += 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stacks = []
        heights = []
        node = root
        h = 0
        min_height = 99999999
        while len(stacks) > 0 or node is not None:
            while node is not None:
                h += 1
                stacks.append(node)
                heights.append(h)
                node = node.left
            node = stacks.pop(-1)
            h = heights.pop(-1)
            if node.right is None:
                min_height = min(h, min_height)
        return min_height
