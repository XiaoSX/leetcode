#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/19
'''

class Solution:

    # 入栈时, 加左括号, 同时保存右括号
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ''
        if root is None:
            return ans

        stack = []
        node = root
        while node is not None or len(stack) > 0:
            while node is not None and node != ')':
                ans += '(' + str(node.val)
                stack.append(')')
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            if node == ')':
                ans += node
                node = None
                continue
            if node.left is None and node.right is not None:
                ans += '()'
            node = node.right

        return ans[1:-1]
