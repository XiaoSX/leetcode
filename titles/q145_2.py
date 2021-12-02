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
        pre_node = None
        node = root
        ans = []
        while node or len(stacks) > 0:
            if node:
                stacks.append(node)
                node = node.left
            else:
                node = stacks[-1]
                # 转右
                if node.right and pre_node != node.right:
                    node = node.right
                # 从右边子树返回
                else:
                    node = stacks.pop(-1)
                    ans.append(node.val)
                    pre_node = node
                    node = None
        return ans