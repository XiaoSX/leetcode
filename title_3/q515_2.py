#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/24
'''

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: TreeNode, curHeight: int) -> None:
            if node is None:
                return
            if curHeight == len(ans):
                ans.append(node.val)
            else:
                ans[curHeight] = max(ans[curHeight], node.val)
            dfs(node.left, curHeight + 1)
            dfs(node.right, curHeight + 1)
        dfs(root, 0)
        return ans
