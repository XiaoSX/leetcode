# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 上午10:26
# @Author  : RenMeng
# @File    : q103.py

from titles.tree import TreeNode
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
                children.append(node.val)
                if node.left is not None:
                    queues.append(node.left)
                if node.right is not None:
                    queues.append(node.right)
            flag *= -1
            if flag == 1:
                ans.append(children)
            else:
                ans.append(list(reversed(children)))
        return ans
