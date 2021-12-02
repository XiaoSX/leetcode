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

        stack = []
        stack_sums = []
        node = root
        total = 0
        while len(stack) > 0 or node is not None:
            while node is not None:
                total += node.val
                stack.append(node)
                stack_sums.append(total)
                node = node.left
            node = stack.pop(-1)
            total = stack_sums.pop(-1)
            if node.left is None and node.right is None and total == targetSum:
                return True
            node = node.right
        return False