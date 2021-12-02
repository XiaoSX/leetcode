#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-07-31
'''
from titles.tree import TreeNode
from titles.listnode import ListNode
class Solution:
    def getPreOrd(self, arr, ans):
        if len(arr) == 0:
            return
        low = 0
        high = len(arr)
        mid = (low + high) // 2
        ans.append(arr[mid])
        self.getPreOrd(arr[low: mid], ans)
        self.getPreOrd(arr[mid+1: high], ans)

    def createTree(self, preord, inord):
        if len(preord) == 0:
            return None
        root = TreeNode(preord[0])
        pi = inord.index(preord[0])
        root.left = self.createTree(preord[1: pi + 1], inord[:pi])
        root.right = self.createTree(preord[pi + 1:], inord[pi + 1:])
        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        inord = []
        while head:
            inord.append(head.val)
            head = head.next
        preord = []
        self.getPreOrd(inord, preord)
        tree = self.createTree(preord, inord)
        return tree
