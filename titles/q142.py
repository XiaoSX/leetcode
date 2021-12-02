#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-03
'''

class Solution:
    def detectCycle(self, head):
        if head is None:
            return None

        p = head.next
        q = head
        while p and p.next and p != q:
            p = p.next.next
            q = q.next
        if p is None or p.next is None:
            return None

        # 环长
        cnt = 1
        q = q.next
        while p != q:
            cnt += 1
            q = q.next

        # 环入口
        p = head
        while 1:
            q = p
            for i in range(cnt):
                q = q.next
            if q == p:
                return p
            p = p.next

