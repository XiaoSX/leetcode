#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-08
'''

from titles.tree import TreeNode
class Solution:
    def postorderTraversal(self, root: TreeNode):
        if root is None:
            return []

        stacks = [root]
        node = root.left
        ans = []

        flag = 0
        while len(stacks) > 0:
            while node:
                stacks.append(node)
                node = node.left

            while node is None or flag == 1:
                if len(stacks) == 0:
                    break

                if len(stacks) > 0 and stacks[-1].left == node:
                    node = stacks[-1]
                    node = node.right
                    if node:
                        flag = 0
                        break
                if len(stacks) > 0 and stacks[-1].right == node:
                    node = stacks.pop(-1)
                    ans.append(node.val)
                    flag = 1

        return ans