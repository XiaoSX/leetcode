# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 下午5:29
# @Author  : RenMeng
# @File    : listnode.py

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
    def __init__(self, value=0):
        self.val = value
        self.next = None