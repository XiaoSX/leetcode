#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/8
'''

from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        root_id = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root_id = i
                break

        root.left = self.buildTree(preorder[1: root_id+1], inorder[:root_id])
        root.right = self.buildTree(preorder[root_id+1:], inorder[root_id+1:])
        return root