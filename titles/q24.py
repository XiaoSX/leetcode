#  -*-  coding: utf-8  -*-


from titles.listnode import ListNode

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy


        while head and head.next:

            pre_node = head
            cur_node = head.next

            pre_node.next = cur_node.next
            cur_node.next = pre_node
            prev_node.next = cur_node

            head = pre_node.next
            prev_node = pre_node


        return dummy.next
