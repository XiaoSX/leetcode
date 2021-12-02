#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-30
'''

from titles.graph import Node

class Solution:

    def __init__(self):
        self.visit = {}

    # def DFS(self, node, visit):
    #     for inode in node.neighbors:
    #         if inode.val not in visit:
    #             inode2 = Node()
    #             inode2.val = inode.val
    #             inode2.neighbors = []
    #             visit[inode.val] = inode2
    #             self.DFS(inode, visit)
    #         visit[node.val].neighbors.append(visit[inode.val])

    # 遍历节点过程中，就可以构建其邻居
    def cloneGraph(self, node):
        if node is None:
            return node

        if node.val in self.visit:
            return node

        clone_node = Node(node.val, [])
        self.visit[node.val] = clone_node # 遍历
        clone_node.neighbors = [self.cloneGraph(inode) for inode in node.neighbors] # 根据原图指导克隆邻居
        return clone_node

