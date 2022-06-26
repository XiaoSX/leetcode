#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/1
'''

from typing import List
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def orderTraversal(root):
            stack = []
            ans = []
            node = root
            while node or len(stack) > 0:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop(-1)
                ans.append(node.val)
                node = node.right
            return ans
        nums1 = orderTraversal(root1)
        nums2 = orderTraversal(root2)
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        ans = []
        while i < m or j < n:
            if (i < m and j < n and nums1[i] < nums2[j]) or j >= n:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        return ans