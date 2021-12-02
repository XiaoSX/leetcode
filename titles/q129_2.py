#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-05-17
'''

from titles.tree import TreeNode
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        cum_sum = 0
        cur_v = 0
        if root is None:
            return 0
        cur_node = root
        stacks = []
        while cur_node or len(stacks) > 0:
            while cur_node:
                cur_v = cur_v * 10 + cur_node.val
                # push update
                cur_node.val = cur_v
                stacks.append(cur_node)
                cur_node = cur_node.left
            # pop recover
            cur_node = stacks.pop(-1)
            cur_v = cur_node.val
            if cur_node.left is None and cur_node.right is None:
                cum_sum += cur_v
            cur_node = cur_node.right
        return cum_sum