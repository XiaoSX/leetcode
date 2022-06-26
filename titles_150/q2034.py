#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/23
'''


class ListNode:
    def __init__(self, value=0):
        self.val = value
        self.next = None
        self.pri = None

class StockPrice:

    def __init__(self):
        self.stocks = {}
        self.cur = -1
        self.head = ListNode(-1)
        self.head.next = self.head
        self.head.pri = self.head

    def insert(self, head, node):
        p = head.next
        while p is not None and p != head and node.val > p.val:
            p = p.next
        node.pri = p.pri
        p.pri.next = node
        p.pri = node
        node.next = p


    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.cur:
            self.cur = timestamp

        if timestamp not in self.stocks:
            node = ListNode(price)
            self.stocks[timestamp] = node
            self.insert(self.head, node)
        else:
            node = self.stocks[timestamp]
            node.val = price
            node.next.pri = node.pri
            node.pri.next = node.next
            node.pri = None
            node.next = None
            self.insert(self.head, node)


    def current(self) -> int:
        return self.stocks[self.cur].val

    def maximum(self) -> int:
        return self.head.pri.val

    def minimum(self) -> int:
        return self.head.next.val

