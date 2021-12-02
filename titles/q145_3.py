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
        stacks = []
        node = root
        ans = []
        while node or len(stacks) > 0:
            if node:
                stacks.append(node)
                node = node.left
            else:
                if stacks[-1].right is None:
                    node = stacks.pop(-1)
                    ans.append(node.val)
                    node = node.right
                else:
                    node = stacks[-1].right
                    stacks[-1].right = None

        return ans