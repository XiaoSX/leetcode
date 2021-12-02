# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午2:45
# @Author  : RenMeng
# @File    : q99.py

from titles.tree import TreeNode
# 交换两个数就保证有序, 一定存在最多两组的逆序关系
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stacks = []
        pre_node = None
        x_node = None
        y_node = None
        cur_node = root
        while cur_node is not None or len(stacks) > 0:
            while cur_node is not None:
                stacks.append(cur_node)
                cur_node = cur_node.left
            cur_node = stacks.pop()
            if pre_node is not None and pre_node.val > cur_node.val:
                y_node = cur_node
                if x_node is None:
                    x_node = pre_node
            pre_node = cur_node
            cur_node = cur_node.right


        tmp = x_node.val
        x_node.val = y_node.val
        y_node.val = tmp