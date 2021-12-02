#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-20
'''

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root is None:
            return False

        queues = [(root, root.val)]
        while len(queues) > 0:
            node, total = queues.pop(0)
            if node.left is None and node.right is None and total == targetSum:
                return True
            if node.left is not None:
                queues.append((node.left, total + node.left.val))
            if node.right is not None:
                queues.append((node.right, total + node.right.val))
        return False