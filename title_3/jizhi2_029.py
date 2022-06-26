#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/18
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # None
        if head is None:
            head = Node(insertVal)
            head.next = head
            return head

        # single Node
        pre = head
        if pre.next == pre:
            cur = Node(insertVal)
            pre.next = cur
            cur.next = pre
            return head

        # same Node val
        cur = pre.next
        while pre.val == cur.val:
            pre = pre.next
            cur = cur.next
            if pre == head:
                new_node = Node(insertVal)
                new_node.next = pre.next
                pre.next = new_node
                return head

        # others
        pre = head
        cur = pre.next
        while True:
            cond1 = (pre.val == insertVal)
            cond2 = (pre.val < insertVal) and (cur.val >= insertVal)  # normal
            cond3 = (pre.val < insertVal) and (pre.val > cur.val)    # max
            # min
            cond4 = (pre.val > insertVal) and (pre.val > cur.val) and (cur.val > insertVal)
            if cond1 or cond2 or cond3 or cond4:
                new_node = Node(insertVal)
                new_node.next = pre.next
                pre.next = new_node
                return head
            pre = pre.next
            cur = cur.next