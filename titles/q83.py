# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午6:06
# @Author  : RenMeng
# @File    : q83.py

from titles.listnode import ListNode
# 只用一个节点就可以
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head