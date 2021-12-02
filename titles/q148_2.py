#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-16
'''
from titles.listnode import ListNode
# class Solution:
#     def combine(self, p, n):
#         dummy = ListNode(0)
#         node = dummy
#         while p and n:
#             if p.val < n.val:
#                 node.next = p
#                 p = p.next
#             else:
#                 node.next = n
#                 n = n.next
#             node = node.next
#         if p is not None:
#             node.next = p
#         if n is not None:
#             node.next = n
#         return dummy.next
#
#     def sortList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#
#         first_p = head
#         second_p = head
#         pri_first = None
#         while second_p and second_p.next:
#             pri_first = first_p
#             first_p = first_p.next
#             second_p = second_p.next.next
#         if pri_first:
#             pri_first.next = None
#         pri = self.sortList(head)
#         nex = self.sortList(first_p)
#         return self.combine(pri, nex)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next
