#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-04
'''

from titles.listnode import ListNode
class Solution:
    def order(self, p, q, depth):
        if depth == 0:
            return q

        q = self.order(p.next, q, depth - 1)
        tmp = q.next
        q.next = p.next
        p.next = q
        q = tmp
        return q

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cnt = 0
        p = head
        while p:
            p = p.next
            cnt += 1

        if cnt % 2 == 0:
            l_cnt = cnt // 2
        else:
            l_cnt = cnt // 2 + 1

        p = head
        q = None
        for i in range(l_cnt):
            q = p
            p = p.next

        q.next = None

        self.order(head, p, cnt // 2)
