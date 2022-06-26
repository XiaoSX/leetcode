#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/30
'''

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        node = root
        stack = []
        val = 0
        pre = None
        while node is not None or len(stack) > 0:
            while node is not None:
                val = val << 1 | node.val
                stack.append(node)
                node = node.left
            node = stack[-1]
            # node.right = None or node.right == pre 的时候出栈
            if node.right is None or node.right == pre:
                if node.left is None and node.right is None:
                    ans += val
                val >>= 1
                stack.pop()
                # 输出
                pre = node
                node = None
            else:
                node = node.right

        return ans
