#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-01
'''

from titles.tree import TreeNode
class Solution:
    def preOrder(self, root, order=True):
        ans =[]
        stacks = []
        while root or len(stacks) > 0:
            while root:
                ans.append(root.val)
                stacks.append(root)
                if not order:
                    root = root.right
                else:
                    root = root.left
            ans.append(99999)
            root = stacks.pop(-1)
            if not order:
                root = root.left
            else:
                root = root.right
        return ans

    def midOrder(self, root, order=True):
        ans = []
        stacks = []
        while root or len(stacks) > 0:
            while root:
                stacks.append(root)
                if not order:
                    root = root.right
                else:
                    root = root.left
            ans.append(99999)
            root = stacks.pop(-1)
            ans.append(root.val)
            if not order:
                root = root.left
            else:
                root = root.right
        return ans

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        pre = self.preOrder(root.left)
        pre1 = self.preOrder(root.right, order=False)
        if pre != pre1:
            return False
        mid = self.midOrder(root.left)
        mid2 = self.midOrder(root.right, order=False)
        if mid != mid2:
            return False
        return True