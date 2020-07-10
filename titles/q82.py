#  -*-  coding: utf-8  -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 头结点没有断开， 如果没有重新连接，将返回origin one
# 尾节点没有断开。
# 头结点为空
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        cur = head

        while head:
            if head.val == cur.val:
                pass
            elif cur.next == head:
                pre.next = cur
                pre = pre.next
                cur = head
            else:
                cur = head
            head = head.next

        if cur is not None and cur.next is None:
            pre.next = cur
            pre = pre.next
        else:
            pre.next = None

        return dummy.next