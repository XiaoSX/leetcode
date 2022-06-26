#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/12
'''

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def commonNode(head1, head2):
    node = head1
    m = 0
    while node:
        node = node.next
        m += 1

    node = head2
    n = 0
    while node:
        node = node.next
        n += 1

    p = head1
    while m > n:
        p = p.next
        m -= 1

    q = head2
    while n > m:
        q = q.next
        q -= 1

    while p and q:
        if p == q:
            return p
        p = p.next
        q = q.next

    return None


final_ans = []

def Sum(arr, target, ans):
    if len(arr) == 0:
        return
    if len(arr) == 1 and arr[0] == target:
        final_ans.append(list(ans) + [arr[0]])
        return


    Sum(arr[1:], target - arr[0], [arr[0]] + ans)
    Sum(arr[1:], target, ans)


