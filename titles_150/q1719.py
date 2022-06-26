#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/16
'''
from typing import List
class Solution:

    def is_root(self, node, degrees):
        degree_cp = {k:v for k, v in degrees}
        children = degree_cp[node]
        if len(children) + 1 != len(degree_cp):
            return 0

        del degree_cp[node]
        for ch_node in children:
            degree_cp[ch_node].remove(node)
        degree_cp = sorted(degree_cp.items(), key=lambda x:len(x[1]), reverse=True)
        n = len(degree_cp)
        for i in range(n):
            pass



    def checkWays(self, pairs: List[List[int]]) -> int:
        degrees = {}
        for x, y in pairs:
            if x not in degrees:
                degrees[x] = set()
            degrees[x].add(y)
            if y not in degrees:
                degrees[y] = set()
            degrees[y].add(x)

        degrees = sorted(degrees.items(), key=lambda x: len(x), reverse=True)
        n = len(degrees)
        i = 0
        root_degree = 0
        flag = 0
        while i < n and len(degrees[i][1]) >= root_degree:
            root_degree = len(degrees[i][1])
            flag += self.is_root(degrees[i][0], degrees)
            if flag >= 2:
                return flag
            i += 1
        return flag