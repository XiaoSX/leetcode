0#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/8
'''

from typing import List
# 维护一个前驱+方向指针
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        stack = []
        pi = 0
        mi = 0
        n = len(preorder)
        if n == 0:
            return None

        root = TreeNode(preorder[0])
        stack.append(root)
        pre_node = root
        pre_flag = 0
        pi += 1

        while mi < n:
            if len(stack) > 0 and inorder[mi] == stack[-1].val:
                pre_node = stack.pop(-1)
                pre_flag = 1
                mi += 1
            else:
                node = TreeNode(preorder[pi])
                if pre_flag == 0:
                    pre_node.left = node
                else:
                    pre_node.right = node
                pre_node = node
                stack.append(node)
                pre_flag = 0
                pi += 1

        return root



