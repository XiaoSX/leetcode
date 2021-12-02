#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

from titles.graph import Node

class Solution:
    def cloneGraph(self, node):
        root = None
        if node is None:
            return root

        # 初始化
        queues = [node]
        node2 = Node(node.val, [])
        visit = {node.val: node2}

        while queues:
            # 出队
            curnode = queues.pop()
            for inode in curnode.neighbors:
                if inode.val not in visit:
                    inode2 = Node(inode.val, [])
                    queues.append(inode)
                    visit[inode.val] = inode2
                visit[curnode.val].neighbors.append(visit[inode.val])
        return visit[node.val]



