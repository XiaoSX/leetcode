#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-08-09
'''

from titles.node import Node

class Solution:
    def subTreeConnect(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        self.subTreeConnect(root.left)
        self.subTreeConnect(root.right)
        left_node = root.left
        right_node = root.right
        while left_node and right_node:
            left_node.next = right_node
            left_node = left_node.right
            right_node = right_node.left


    def connect(self, root: Node) -> Node:
        if root is None:
            return root

        self.subTreeConnect(root)
        node = root
        while node:
            node.next = None
            node = node.right
        return root