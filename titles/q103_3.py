# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 上午11:57
# @Author  : RenMeng
# @File    : q103_3.py

from titles.tree import TreeNode
# list 的头插和尾插
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return []
        queues = [root]
        ans = []
        flag = -1
        while len(queues) > 0:
            children_size = len(queues)
            children = []
            for i in range(children_size):
                node = queues.pop(0)
                if flag == -1:
                    children.append(node.val)
                else:
                    children.insert(0, node.val)
                if node.left is not None:
                    queues.append(node.left)
                if node.right is not None:
                    queues.append(node.right)
            flag *= -1
            ans.append(children)
        return ans
