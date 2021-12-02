# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 下午2:26
# @Author  : RenMeng
# @File    : q86.py
from titles.q24 import ListNode

class Solution:
    # pay attention to the end of the list, 链表结束后的指针重置为None的问题
    def partition(self, head, x: int):
        first_walk = ListNode(-1)
        second_walk = ListNode(-1)
        first_head = first_walk # first_head 和 first_walk 指向同一个对象, first_walk用来链接对象指针
        second_head = second_walk
        walk = head
        while walk:
            if walk.val >= x:
                second_walk.next = walk
                second_walk = second_walk.next
            else:
                first_walk.next = walk
                first_walk = first_walk.next
            walk = walk.next

        first_walk.next = second_head.next
        second_walk.next = None
        return first_head.next