#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-11-15
'''

from titles.tree import TreeNode
from titles.tree import createTrees
# class Solution:
#     def sortedArrayToBST(self, nums) -> TreeNode:
#         if len(nums) == 0:
#             return None
#         root_i = len(nums) // 2
#         root = TreeNode(nums[root_i])
#         root.left = self.sortedArrayToBST(nums[:root_i])
#         root.right = self.sortedArrayToBST(nums[root_i + 1:])
#         return root

def createTrees(pri_order, mid_order):
    if len(pri_order) == 0 and len(mid_order) == 0:
        return None
    root = TreeNode()
    root.val = pri_order[0]
    flag = -1
    for i in range(len(mid_order)):
        if mid_order[i] == root.val:
            flag = i
            break
    root.left = createTrees(pri_order[1:flag+1], mid_order[:flag])
    root.right = createTrees(pri_order[1+flag:], mid_order[1+flag:])
    return root


class Solution:
    def sortedArrayToBST(self, nums):
        process = [nums]
        new_process = []
        while True:
            if all([False if isinstance(x, list) else True for x in process]):
                break
            for i in range(len(process)):
                arr = process[i]
                if not isinstance(arr, list):
                    new_process.append(arr)
                    continue

                ri = len(arr) // 2
                new_process.append(arr[ri])
                if ri > 0:
                    new_process.append(arr[:ri])
                if ri + 1 < len(arr):
                    new_process.append(arr[ri+1:])
            process = list(new_process)
            new_process = []

        return createTrees(process, nums)