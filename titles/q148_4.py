#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-21
'''

from titles.listnode import ListNode
class Solution:
    def quicksort(self, head):
        if head is None or head.next is None:
            return head, head

        pivot = head
        p = head.next
        dummy = ListNode(0)
        dummy.next = p
        q = dummy
        pivot.next = None

        while p:
            if p.val < pivot.val:
                q = p
                p = p.next
            else:
                q.next = p.next
                p.next = pivot.next
                pivot.next = p
                p = q.next

        fhead, ftail = self.quicksort(dummy.next)
        shead, stail = self.quicksort(pivot.next)
        if fhead is None and ftail is None:
            pivot.next = shead
            return pivot, stail
        ftail.next = pivot
        pivot.next = shead
        if shead is None and stail is None:
            return fhead, pivot
        return fhead, stail

    def sortList(self, head: ListNode) -> ListNode:
        head, _ = self.quicksort(head)
        return head