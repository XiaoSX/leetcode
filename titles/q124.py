#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-04
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from titles.tree import TreeNode
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def getmax(root):
            if root.left is None and root.right is None:
                return root.val, root.val

            path = root.val
            max_path = root.val
            cur_path = root.val
            if root.left is not None:
                left_v, max_left_v = getmax(root.left)
                cur_path = root.val + left_v
                max_path = max(left_v, max_left_v, cur_path, root.val)
                path = max(root.val, root.val + left_v)
            if root.right is not None:
                right_v, max_right_v = getmax(root.right)
                max_path = max(max_path, right_v, max_right_v, cur_path + right_v, right_v + root.val, root.val)
                path = max(path, root.val + right_v)

            return path, max_path

        root_v, max_v = getmax(root)
        return max_v