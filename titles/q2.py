#  -*-  coding: utf-8  -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def input_node(list_a):
    pre = None
    head = pre
    for i in list_a:
        ele = ListNode(i)
        if pre is not None:
            pre.next = ele
        pre = ele
        if head is None:
            head = pre
    return head

def output_node(List_a):
    ans = []
    while List_a is not None:
        ans.append(List_a.val)
        List_a = List_a.next
    return ans


class Solution:
    def addTwoNumbers(self, l1, l2):
        pre = None
        head = pre
        unit = 0
        while l1 is not None and l2 is not None:
            ans = ListNode(int((l1.val + l2.val + unit) % 10))
            unit = int((l1.val + l2.val + unit) / 10)
            if pre is not None:
                pre.next = ans
            pre = ans
            if head is None:
                head = pre
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            ans = ListNode(int((l1.val + unit) % 10))
            unit = int((l1.val + unit) / 10)
            if pre is not None:
                pre.next = ans
            pre = ans
            if head is None:
                head = pre
            l1 = l1.next
        while l2 is not None:
            ans = ListNode(int((l2.val + unit) % 10))
            unit = int((l2.val + unit) / 10)
            if pre is not None:
                pre.next = ans
            pre = ans
            if head is None:
                head = pre
            l2 = l2.next
        if unit > 0:
            ans = ListNode(unit)
            pre.next = ans

        return head