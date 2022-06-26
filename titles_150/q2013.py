#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/26
'''
from typing import List

class DetectSquares:

    def __init__(self):
        self.memory = {}
        self.index = 0
        self.coor_xs = [set() for _ in range(1001)]
        self.coor_ys = [set() for _ in range(1001)]


    def add(self, point: List[int]) -> None:
        x, y = point
        self.coor_xs[x].add(self.index)
        self.coor_ys[y].add(self.index)
        self.memory[self.index] = point
        self.index += 1


    def count(self, point: List[int]) -> int:
        px, py = point
        points_x = self.coor_xs[px]
        points_y = self.coor_ys[py]

        px_all_y = set()
        seen_y = set()
        for p in points_x:
            y = self.memory[p][1]
            if y not in seen_y:
                seen_y.add(y)
                px_all_y = px_all_y.union(self.coor_ys[y])


        py_all_x = set()
        seen_x = set()
        for p in points_y:
            x = self.memory[p][0]
            if x not in seen_x:
                seen_x.add(x)
                py_all_x = py_all_x.union(self.coor_xs[x])


        px_all_y = px_all_y.difference(points_x)
        py_all_x = py_all_x.difference(points_y)


        canditate = px_all_y.intersection(py_all_x)
        count = 0
        for p in canditate:
            x, y = self.memory[p]
            if abs(x- px) != abs(y-py):
                continue
            m = len(self.coor_xs[x].intersection(points_y))
            n = len(self.coor_ys[y].intersection(points_x))

            count += m * n
        return count
