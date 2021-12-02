#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-15
'''

from titles.listnode import ListNode
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last_sorted = head
        p = head.next
        while p:
            q = dummy
            while q.next and q.next.val < p.val:
                q = q.next
            last_sorted.next = p.next
            p.next = q.next
            q.next = p
            p = last_sorted.next
        return dummy.next