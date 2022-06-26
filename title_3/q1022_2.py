#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/30
'''

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, val):
            if node is None:
                return val

            val = val << 1 | node.val
            if node.left is None and node.right is None:
                return val

            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)
