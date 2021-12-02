#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-09
'''

from titles.node import Node

class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return root
        node = root
        queues = [node, '#']
        pre_node = None
        while len(queues) > 0:
            node = queues.pop(0)
            if node == '#':
                pre_node.next = None
                pre_node = None
                if len(queues) > 0:
                    queues.append('#')
                continue
            if node.left and node.right:
                queues.append(node.left)
                queues.append(node.right)
            if pre_node:
                pre_node.next = node
            pre_node = node
        return root
