#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-07
'''

from titles.tree import TreeNode
class Solution:
    def subPathSum(self, root, target, ans, total_ans):
        if root is None:
            return

        if root.left is None and root.right is None and target == root.val:
            ans.append(root.val)
            total_ans.append(ans[:])
            ans.pop(-1)
            return
        ans.append(root.val)
        target -= root.val
        self.subPathSum(root.left, target, ans, total_ans)
        self.subPathSum(root.right, target, ans, total_ans)
        ans.pop(-1)
        target += root.val

    def pathSum(self, root: TreeNode, targetSum: int):
        total_ans = []
        ans = []
        self.subPathSum(root, targetSum, ans, total_ans)
        return total_ans