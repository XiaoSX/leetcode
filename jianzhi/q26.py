#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/29
'''

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def subTree(tree1, tree2):
            if tree2 is None:
                return True

            if tree1 is None:
                return False

            if tree1.val != tree2.val:
                return False

            return subTree(tree1.left, tree2.left) & subTree(tree1.right, tree2.right)


        if A is None or B is None:
            return False

        root = subTree(A, B)
        if root:
            return True
        left_tree = self.isSubStructure(A.left, B)
        if left_tree:
            return True
        right_tree = self.isSubStructure(A.right, B)
        if right_tree:
            return True
        return False

