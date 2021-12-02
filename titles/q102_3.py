# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 上午10:23
# @Author  : RenMeng
# @File    : q102_3.py

from titles.tree import TreeNode
class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        queues = [root]
        ans = []
        while len(queues) > 0:
            child_value = []
            children_size = len(queues)
            for i in range(children_size):
                node = queues.pop(0)
                child_value.append(node.val)
                if node.left is not None:
                    queues.append(node.left)
                if node.right is not None:
                    queues.append(node.right)
            ans.append(child_value)
        return ans
