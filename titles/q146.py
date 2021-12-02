#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-09-06
'''

# 下标和元素值搞混淆
class LRUCache:

    def __init__(self, capacity: int):
        self.time = 0
        self.c = capacity
        self.momery = {}  # {key: [value, queue_id]}
        self.queue = []  # 小顶堆 [[key, time]]

    def adjust(self, qid):
        n = len(self.queue)
        non_leaf_node = n // 2 - 1
        while qid <= non_leaf_node:
            left_c = 2 * qid + 1
            right_c = 2 * qid + 2
            if right_c >= n or self.queue[left_c][1] < self.queue[right_c][1]:
                self.momery[self.queue[qid][0]][1] = left_c
                self.momery[self.queue[left_c][0]][1] = qid
                self.queue[qid], self.queue[left_c] = self.queue[left_c], self.queue[qid]
                qid = left_c
            else:
                self.momery[self.queue[qid][0]][1] = right_c
                self.momery[self.queue[right_c][0]][1] = qid
                self.queue[qid], self.queue[right_c] = self.queue[right_c], self.queue[qid]
                qid = right_c

    def get(self, key: int) -> int:
        if key not in self.momery:
            return -1
        qid = self.momery[key][1]
        self.queue[qid][1] = self.time
        self.time += 1
        self.adjust(qid)
        return self.momery[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.momery:
            self.momery[key][0] = value
            qid = self.momery[key][1]
            self.queue[qid][1] = self.time
            self.time += 1
            self.adjust(qid)
        else:
            if len(self.queue) == self.c:
                del self.momery[self.queue[0][0]]
                if self.c == 1:
                    self.queue = []
                else:
                    self.momery[self.queue[self.c-1][0]][1] = 0
                    self.queue[0], self.queue[self.c-1] = self.queue[self.c-1], self.queue[0]
                    self.queue = self.queue[:self.c-1]
                    self.adjust(0)
            self.queue.append([key, self.time])
            self.time += 1
            self.momery[key] = [value, len(self.queue) - 1]