#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-19
'''
from titles.listnode import ListNode
# 迭代：首尾指针，head，tail
# 迭代结束条件
# combine： 链表的结束指针，循环的结束条件不是None，combine的两个链表有一个为空
class Solution:
    def combine(self, p, p_end, n, n_end):
        if n is None:
            node = p
            while node.next != p_end:
                node = node.next
            return p, node
        dummy = ListNode(0)
        node = dummy
        while p != p_end and n != n_end:
            if p.val < n.val:
                node.next = p
                p = p.next
            else:
                node.next = n
                n = n.next
            node = node.next
        flag = 0
        if p != p_end:
            node.next = p
            flag = 1
        if n != n_end:
            node.next = n
            flag = 2
        while node.next:
            if flag == 1 and node.next != p_end:
                node = node.next
            elif flag == 2 and node.next != n_end:
                node = node.next
            else:
                break
        return dummy.next, node

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        step = 1
        pre_h = head
        while True:
            first_p = pre_h
            second_p = pre_h
            first_end = pre_h
            seconde_end = pre_h
            pre_t = None
            pre_h = None
            flag = 0
            while True:
                for i in range(step):
                    if second_p:
                        second_p = second_p.next
                    else:
                        flag = 1
                        break
                if flag == 1:
                    flag = 0
                    if pre_t is not None:
                        pre_t.next = first_p
                    else:
                        return first_p
                    break
                first_end = second_p
                seconde_end = second_p
                for i in range(step):
                    if seconde_end:
                        seconde_end = seconde_end.next
                    else:
                        break
                h, t = self.combine(first_p, first_end, second_p, seconde_end)
                t.next = None
                if pre_h is None:
                    pre_h = h
                if pre_t is not None:
                    pre_t.next = h
                pre_t = t
                first_p = seconde_end
                second_p = seconde_end
                first_end = seconde_end
                seconde_end = seconde_end
                if first_p is None:
                    break
            step *= 2