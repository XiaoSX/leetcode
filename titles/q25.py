#  -*-  coding: utf-8  -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        pre_head = dummy
        first_node = head

        while first_node:
            pre_tail = first_node
            second_node = first_node.next
            pre_tail.next = None
            p = k

            while p > 1 and second_node:
                next_node = second_node.next
                second_node.next = first_node
                first_node = second_node
                second_node = next_node
                p -= 1

            if p > 1:
                pre_tail = first_node
                second_node = first_node.next
                while second_node:
                    next_node = second_node.next
                    second_node.next = first_node
                    first_node = second_node
                    second_node = next_node

                pre_head.next = first_node
                pre_tail.next = None
                break

            pre_head.next = first_node
            pre_head = pre_tail
            first_node = second_node

        return dummy.next

