#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/31
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 两个链表相交，公共长度必然>linknode_1 and > linknode_2
class Solution:
    def getIntersectionNode(self, headA, headB):
        node = headA
        n = 0
        while node:
            n += 1
            node = node.next

        node = headB
        m = 0
        while node:
            m += 1
            node = node.next

        node_1 = headA
        node_2 = headB
        while n > m:
            node_1 = node_1.next
            n -= 1
        while m > n:
            node_2 = node_2.next
            m -= 1
        while node_1 != node_2:
            node_1 = node_1.next
            node_2 = node_2.next

        return node_1
