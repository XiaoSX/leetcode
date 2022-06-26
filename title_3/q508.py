#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/19
'''

class Solution:
    def __init__(self):
        self.ans = {}

    def getSum(self, node):
        if node is None:
            return 0

        node_sum = node.val + self.getSum(node.left) + self.getSum(node.right)
        if node_sum not in self.ans:
            self.ans[node_sum] = 0
        self.ans[node_sum] += 1
        return node_sum

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.getSum(root)
        ans = sorted(self.ans.items(), key=lambda x:x[1], reverse=True)
        if len(ans) == 0:
            return []
        result = []
        max_v = ans[0][1]
        for k, v in ans:
            if v < max_v:
                break
            result.append(k)
        return result
