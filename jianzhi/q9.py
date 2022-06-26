#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/22
'''

class CQueue:

    def __init__(self):
        self.getin = []
        self.getout = []

    def appendTail(self, value: int) -> None:
        self.getin.append(value)


    def deleteHead(self) -> int:
        if len(self.getout) == 0:
            if len(self.getin) == 0:
                return -1
            while len(self.getin) > 0:
                ele = self.getin.pop(-1)
                self.getout.append(ele)
            return self.getout.pop(-1)
        return self.getout.pop(-1)