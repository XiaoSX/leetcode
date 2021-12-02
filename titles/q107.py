#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-31
'''
from titles.tree import TreeNode
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        queue = []
        ans = []
        if root is None:
            return ans
        queue.append(root)
        queue.append('#')
        ans.append([])
        while len(queue) > 0:
            node = queue.pop(0)
            if node == '#':
                if len(queue) > 0:
                    queue.append('#')
                    ans.append([])
                continue
            ans[-1].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans[::-1]