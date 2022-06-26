#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/16
'''


class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        ans = []
        stack = []
        node = root
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            ans.append(node.val)
            node = node.right

        v_map = {}
        for i in range(len(ans)):
            v_map[ans[i]] = i

        color = [0 for _ in range(len(ans))]
        for i in range(len(ops)):
            t, x, y = ops[i]
            for j in range(v_map[x], v_map[y] + 1):
                color[j] = t

        return sum(color)
