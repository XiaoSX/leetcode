#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/21
'''

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node = root
        ans = []
        stack = []
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            ans.append(node.val)
            node = node.right

        n = len(ans)
        low = 0
        high = n - 1
        while low < high:
            a = ans[low]
            b = ans[high]
            if a + b == k:
                return True
            if a + b > k:
                high -= 1
            else:
                low += 1
        return False