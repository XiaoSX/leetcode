#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-26
'''

from titles.tree import TreeNode
# 子循环可能越界的问题
# 迭代前序遍历，利用栈顶元素，前序的出栈顺序==中序的遍历顺利
# 用栈顶做判断条件
# 前序，栈顶（移动的）在中序中不遇到自己，前序迭代的所有元素都是栈顶的左孩子
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        stack = []
        n = len(preorder)
        if n == 0:
            return None
        root = TreeNode(preorder[0])
        stack.append(root)
        inorderIndex = 0
        for i in range(1, n):
            node = stack[-1]
            # 一路向左，直到找到最左节点，栈里经过的所有节点均是其父亲的左孩子，前序里栈顶不遇到自己（中序）前的节点都是其父辈
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorder[i])
                stack.append(node.left)
            # 根节点出栈，挂其右孩子，右孩子指向前序的当前节点
            # 如果右孩子为空，栈顶的元素该继续出栈（挂其父母的右孩子）
            else:
                while len(stack) > 0 and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop(-1)
                    inorderIndex += 1
                node.right = TreeNode(preorder[i])
                stack.append(node.right)

        return root

