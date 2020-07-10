#  -*-  coding: utf-8  -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        first_node = dummy
        cur_node = dummy

        while n > 0 and first_node:
            first_node = first_node.next
            n -= 1
        if n > 0:
            return dummy.next

        while first_node and first_node.next:
            first_node = first_node.next
            cur_node = cur_node.next

        cur_node.next = cur_node.next.next
        return dummy.next
