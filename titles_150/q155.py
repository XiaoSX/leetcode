#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-06
'''

class MinStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.n = 0


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.heap) <= self.n:
            self.heap.append(val)
        else:
            self.heap[self.n - 1] = val
        self.n += 1
        j = self.n - 1
        parent = (j - 1) // 2
        while parent >= 0 and self.heap[j] < self.heap[parent]:
            self.heap[j], self.heap[parent] = self.heap[parent], self.heap[j]
            j = parent
            parent = (j - 1) // 2

    def pop(self) -> None:
        val = self.stack.pop(-1)
        i = 0
        while i < self.n:
            if self.heap[i] == val:
                break
            i += 1
        self.heap[i], self.heap[self.n-1] = self.heap[self.n-1], self.heap[i]
        self.n -= 1
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        while True:
            if left_child < self.n and right_child < self.n:
                if self.heap[left_child] < self.heap[right_child] and self.heap[left_child] < self.heap[i]:
                    self.heap[i], self.heap[left_child] = self.heap[left_child], self.heap[i]
                    i = left_child
                elif self.heap[left_child] >= self.heap[right_child] and self.heap[right_child] < self.heap[i]:
                    self.heap[i], self.heap[right_child] = self.heap[right_child], self.heap[i]
                    i = right_child
                else:
                    break
            elif left_child < self.n and self.heap[left_child] < self.heap[i]:
                self.heap[i], self.heap[left_child] = self.heap[left_child], self.heap[i]
                i = left_child
            else:
                break
            left_child = 2 * i + 1
            right_child = 2 * i + 2


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if self.n > 0:
            return self.heap[0]
        else:
            return None