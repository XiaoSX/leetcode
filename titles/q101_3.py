#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-08
'''

from titles.tree import TreeNode
class Solution:
    def checkSysmetric(self, arr):
        n = len(arr)
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        for i in range(n // 2):
            j = n - 1 - i
            if arr[i] != arr[j]:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queues = [root, '#']
        level_eles = []
        while len(queues) > 0:
            node = queues.pop(0)
            if node == '#':
                if not self.checkSysmetric(level_eles):
                    return False
                if set(level_eles) == '#':
                    return True
                level_eles = []
                if len(queues) == 0:
                    break
                else:
                    queues.append('#')
                    continue
            if node is None:
                level_eles.append('#')
                continue
            level_eles.append(node.val)
            queues.append(node.left)
            queues.append(node.right)

        return True