#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-01
'''

class Solution:
    # 注意next为空的情况时，避免出现next.next
    def copyRandomList(self, head):
        if head is None:
            return

        node = head
        while node:
            node_cp = Node(node.val)
            node_cp.next = node.next
            node.next = node_cp
            node = node_cp.next

        node = head
        while node:
            node_cp = node.next
            if node.random is None:
                node_cp.random = node.random
            else:
                node_cp.random = node.random.next
            node = node_cp.next

        node = head
        head_cp = node.next
        while node:
            node_cp = node.next
            node.next = node_cp.next
            if node_cp.next is not None:
                node_cp.next = node_cp.next.next
            else:
                node_cp.next = None
            node = node.next
        return head_cp