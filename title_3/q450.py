#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/2
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        if root is None:
            return root

        stack = []
        pre = None
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right == pre:
                pre = stack.pop()
                if pre.val == key:
                    break
                node = None
            else:
                node = node.right

        if pre.val != key:
            return root

        parent = None
        cur = pre
        if len(stack) > 0:
            parent = stack[-1]

        if cur.left is not None:
            parent = cur
            cur = cur.left
            while cur.right is not None:
                parent = cur
                cur = cur.right
            cur.val, pre.val = pre.val, cur.val
            if parent.right == cur:
                parent.right = cur.left
            else:
                parent.left = cur.left

        else:
            if parent is None:
                return root.right

            if parent.left == cur:
                parent.left = cur.right
            else:
                parent.right = cur.right

        return root

