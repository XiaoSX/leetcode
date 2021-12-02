# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 上午9:36
# @Author  : RenMeng
# @File    : q102.py

from titles.tree import TreeNode
# '#' 表示每层遍历结束, 队列里还有没有遍历到的节点的时候,添加#, else,不添加,防止死循环
class Solution:
    def levelOrder(self, root: TreeNode):
        queues = []
        if root is None:
            return queues
        queues.append(root)
        queues.append('#')
        ans = []
        cur_level = []
        while len(queues) > 0:
            cur = queues.pop(0)
            if cur == '#':
                ans.append(cur_level)
                cur_level = []
                if len(queues) > 0:
                    queues.append('#')
                continue
            cur_level.append(cur.val)
            if cur.left is not None:
                queues.append(cur.left)
            if cur.right is not None:
                queues.append(cur.right)
        return ans


