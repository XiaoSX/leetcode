#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/8
'''

from typing import List
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        ans = []
        while len(queue) > 0:
            q_size = len(queue)
            level_nodes = []
            for i in range(q_size):
                node = queue[i]
                level_nodes.append(node.val)
                for child in node.children:
                    queue.append(child)
            queue = queue[q_size:]
            ans.append(level_nodes)
        return ans