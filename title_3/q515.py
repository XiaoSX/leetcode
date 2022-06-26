#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/24
'''

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        queue = [root]
        while len(queue) > 0:
            max_v = float('-inf')
            q_size = len(queue)
            for i in range(q_size):
                node = queue[i]
                if node.val > max_v:
                    max_v = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            queue = queue[q_size:]
            ans.append(max_v)
        return ans