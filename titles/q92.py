# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午5:28
# @Author  : RenMeng
# @File    : q92.py

from titles.listnode import ListNode
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur_node = dummy
        pre_node = dummy
        cnt = 0
        while cnt <= n:
            if cnt == m:
                new_tail = cur_node
                old_tail = pre_node

            if cnt < m + 1:
                pre_node = cur_node
                cur_node = cur_node.next
            else:
                next_node = cur_node.next
                cur_node.next = pre_node
                pre_node = cur_node
                cur_node = next_node
            cnt += 1
        new_tail.next = cur_node
        old_tail.next = pre_node

        return dummy.next
