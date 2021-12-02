#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-07
'''
from titles.tree import TreeNode
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        stacks = []
        node = root
        while node or len(stacks) > 0:
            while node:
                stacks.append(node)
                node = node.left
            node = stacks.pop(-1)
            node = node.right