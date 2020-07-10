#  -*-  coding: utf-8  -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        dummy = ListNode(-1)
        pre_node = dummy

        n = len(lists)
        # 删除空链表情况
        for i in range(n-1, -1, -1):
            if lists[i] is None:
                lists.pop(i)
        n = len(lists)

        if n == 0:
            return None

        while n > 1:
            flag = 9999999
            f_i = -1

            for i in range(n):
                if flag > lists[i].val:
                    flag = lists[i].val
                    f_i = i
            pre_node.next = lists[f_i]
            pre_node = pre_node.next
            lists[f_i] = lists[f_i].next
            if lists[f_i] is None:
                lists.pop(f_i)
            n = len(lists)

        if n == 1:
            pre_node.next = lists[0]

        return dummy.next