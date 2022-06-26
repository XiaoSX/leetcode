#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-10
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        prior = None
        self.cur_node = None
        node = root
        stacks = []
        while node or len(stacks) > 0:
            while node:
                stacks.append(node)
                node = node.left
            node = stacks.pop(-1)
            if prior:
                prior.right = node
            prior = node
            if self.cur_node is None:
                self.cur_node = prior
            node = node.right

    def next(self) -> int:
        node = self.cur_node
        if node:
            self.cur_node = self.cur_node.right
        return node

    def hasNext(self) -> bool:
        if self.cur_node:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
