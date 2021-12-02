# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 上午10:23
# @Author  : RenMeng
# @File    : q99_2.py

from titles.tree import TreeNode
# Morris中序遍历, 不需要stack, O(1)的空间复杂度
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        cur_node = root
        ans = []
        while cur_node is not None:
            if cur_node.left is not None:
                most_right_node = cur_node.left
                while most_right_node is not None and most_right_node != cur_node:
                    most_right_node = most_right_node.right
                if most_right_node is None:
                    most_right_node.right = cur_node
                    cur_node = cur_node.left
                else:
                    ans.append(cur_node.val)
                    cur_node = cur_node.right
            else:
                ans.append(cur_node.val)
                cur_node = cur_node.right