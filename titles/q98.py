# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 下午3:07
# @Author  : RenMeng
# @File    : q98.py

# Definition for a binary tree node.
from titles.tree import TreeNode
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stacks = []
        travel = root
        cur = None
        while travel is not None or len(stacks) > 0:
            while travel is not None:
                stacks.append(travel)
                travel = travel.left
            travel = stacks.pop()
            if cur is not None and travel.val <= cur:
                return False
            cur = travel.val
            travel = travel.right
        return True