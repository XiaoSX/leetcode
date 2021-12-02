# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午2:38
# @Author  : RenMeng
# @File    : q94_2.py

from titles.tree import TreeNode
class Solution:
    def inorderTraversal(self, root: TreeNode):
        stacks = []
        ans = []
        travel = root
        while travel is not None or len(stacks) > 0:
            while travel is not None:
                stacks.append(travel)
                travel = travel.left
            travel = stacks.pop()
            ans.append(travel.val)
            travel = travel.right
        return ans