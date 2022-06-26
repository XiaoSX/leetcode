#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/22
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.memory = []
        self.min_v = []

    def push(self, x: int) -> None:
        self.memory.append(x)
        if len(self.min_v) == 0:
            self.min_v.append(x)
        elif self.min_v[-1] <= x:
            self.min_v.append(self.min_v[-1])
        else:
            self.min_v.append(x)

    def pop(self) -> None:
        self.memory.pop(-1)
        self.min_v.pop(-1)

    def top(self) -> int:
        if len(self.memory) > 0:
            return self.memory[-1]
        return -1


    def min(self) -> int:
        if len(self.memory) > 0:
            return self.min_v[-1]
        return -1