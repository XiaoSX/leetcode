#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/6
'''

class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        while len(self.requests) > 0 and self.requests[0] < t - 3000:
            self.requests.pop(0)
        self.requests.append(t)
        return len(self.requests)

