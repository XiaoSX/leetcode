#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-15
'''
from titles.listnode import ListNode
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            r = p.next
            while r:
                if p.val > r.val:
                    p.val, r.val = r.val, p.val
                r = r.next
            p = p.next
        return head

