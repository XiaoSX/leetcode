#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-31
'''

from titles.tree import TreeNode
class Solution:
    def levelOrder(self, root, level, ans):
        if root is None:
            return

        if len(ans) < level + 1:
            ans.append([])
        ans[level].append(root.val)
        self.levelOrder(root.left, level + 1, ans)
        self.levelOrder(root.right, level + 1, ans)

    def levelOrderBottom(self, root: TreeNode):
        level = 0
        ans = []
        self.levelOrder(root, level, ans)
        return ans[::-1]