#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/13
'''


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def postOrder(node):
            if node is None:
                return
            postOrder(node.left)
            postOrder(node.right)
            ans.append(node.val)
        postOrder(root)
        return ' '.join(map(str, ans))


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = map(int, data.split())
        def createTree(low, high):
            if len(data) == 0 or data[-1] < low or data[-1] > high:
                return None

            val = data.pop(-1)
            root = TreeNode(val)
            root.right = createTree(val, high)
            root.left = createTree(low, val)
            return root
        root = createTree(float('-inf'), float('inf'))
        return root