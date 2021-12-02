# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 上午10:41
# @Author  : RenMeng
# @File    : q103_2.py

from titles.tree import TreeNode
# list 的动态变化, 入队的同时又出队
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
            flag *= -1

            for i in range(children_size-1, -1, -1):
                node = queues.pop(i)
                children.append(node.val)
                if flag == 1:
                    if node.left is not None:
                        queues.append(node.left)
                    if node.right is not None:
                        queues.append(node.right)
                else:
                    if node.right is not None:
                        queues.append(node.right)
                    if node.left is not None:
                        queues.append(node.left)
            ans.append(children)
        return ans
