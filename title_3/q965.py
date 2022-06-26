#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/24
'''

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        ans = set()
        stack = []
        node = root
        while node is not None or len(stack) > 0:
            while node:
                ans.add(node.val)
                if len(ans) > 1:
                    return False
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            node = node.right
        return True