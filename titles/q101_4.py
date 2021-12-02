#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-08
'''

from titles.tree import TreeNode
class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True

        queues = [root.left, root.right]
        while len(queues) > 0:
            left = queues.pop(0)
            right = queues.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queues.append(left.right)
            queues.append(right.left)
            queues.append(left.left)
            queues.append(right.right)

        return True