#  -*-  coding: utf-8  -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 维护尾指针即可，形成环后，head=tail.next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        first = head
        last = head
        cnt = 0
        while head:
            cnt += 1
            last = head
            head = head.next
        head = first
        last.next = first

        # first and last右移k
        k = cnt - k % cnt
        while k > 0:
            head = head.next
            last = last.next
            k -= 1
        last.next = None
        return head

