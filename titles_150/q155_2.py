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


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.heap) == 0 or val < self.heap[-1]:
            self.heap.append(val)
        else:
            self.heap.append(self.heap[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.heap.pop(-1)


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if len(self.heap) > 0:
            return self.heap[-1]
        else:
            return None