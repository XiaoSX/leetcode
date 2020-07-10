#  -*-  coding: utf-8  -*-


def create_listnode(arr):
    head = None
    cur = None
    for i in range(len(arr)):
        node = ListNode(arr[i])
        if head is None:
            head = node
        if cur is not None:
            cur.next = node
        cur = node
    return head

def print_listnode(listnode):
    cur = listnode
    ans = []
    while cur is not None:
        ans.append(cur.val)
        cur = cur.next
    print(ans)

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

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
