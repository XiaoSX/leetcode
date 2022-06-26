#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/22
'''

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        leftmost = 0
        queue = [root]
        while len(queue) > 0:
            q_size = len(queue)
            leftmost = queue[0].val
            for i in range(q_size):
                node = queue[i]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            queue = queue[q_size:]

        return leftmost