#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/16
'''

from titles.tree import createTrees
from titles.tree import TreeNode

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        if p.right:
            successor = p.right
            while successor.left:
                successor = successor.left
            return successor
        node = root
        while node:
            if node.val > p.val:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor


if __name__ == '__main__':
    s = Solution()
    pri = [1, 1, 1, 2]
    order = [1, 1, 1, 2]
    root = createTrees(pri, order)
    node = root
    while node.left:
        node = node.left
    print(node.val)
    print(node.left, node.right)
    ans = s.inorderSuccessor(root, node)
    print(ans.val)
