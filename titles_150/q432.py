#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/3/16
'''


class Heap:
    def __init__(self):
        self.memory_min = []
        self.memory_max = []

    def update(self, ith, kind, delta=1):
        if kind == 'min':
            self.memory_min[ith][0] += delta
            index = self.adjust(self.memory_min, ith, kind)
        else:
            self.memory_max[ith][0] += delta
            index = self.adjust(self.memory_max, ith, 'max')
        return index

    def adjust(self, data, ith, key='min'):
        while ith > 0:
            parent = (ith - 1) // 2
            if key == 'min':
                if data[ith][0] < data[parent][0]:
                    data[parent], data[ith] = data[ith], data[parent]
                else:
                    break
            elif key == 'max':
                if data[ith][0] > data[parent][0]:
                    data[parent], data[ith] = data[ith], data[parent]
                else:
                    break
            ith = parent
        return ith


    def adjust_down(self, data, ith, key='min'):
        n = len(self.memory_min)
        left_c = 2 * ith + 1
        right_c = 2 * ith + 2

        while left_c < n:
            if key == 'min':
                if right_c < n and data[ith][0] > data[right_c][0] and data[left_c][0] > data[right_c][0]:
                    data[right_c], data[ith] = data[ith], data[right_c]
                    ith = right_c
                elif data[ith][0] > data[left_c][0]:
                    data[left_c], data[ith] = data[ith], data[left_c]
                    ith = left_c
                else:
                    break
            elif key == 'max':
                if right_c < n and data[ith][0] < data[right_c][0] and data[left_c][0] < data[right_c][0]:
                    data[right_c], data[ith] = data[ith], data[right_c]
                    ith = right_c
                elif data[ith][0] < data[left_c][0]:
                    data[left_c], data[ith] = data[ith], data[left_c]
                    ith = left_c
                else:
                    break
            left_c = 2 * ith + 1
            right_c = 2 * ith + 2

    def insert(self, ele):
        ith = len(self.memory_min)
        self.memory_min.append(ele)
        self.memory_max.append(ele)
        index_min = self.adjust(self.memory_min, ith, 'min')
        index_max = self.adjust(self.memory_max, ith, 'max')
        return index_min, index_max


    def delete(self, ith, kind):
        n = len(self.memory_min)
        if kind == 'min':
            self.memory_min[ith], self.memory_min[n - 1] = self.memory_min[n - 1], self.memory_min[ith]
            self.memory_min = self.memory_min[:-1]
            self.adjust_down(self.memory_min, ith, key='min')
        else:
            self.memory_max[ith], self.memory_max[n - 1] = self.memory_max[n - 1], self.memory_max[ith]
            self.memory_max = self.memory_max[:-1]
            self.adjust_down(self.memory_max, ith, key='max')

class AllOne:

    def __init__(self):
        self.memory_min = {}
        self.memory_max = {}
        self.heap = Heap()

    def inc(self, key: str) -> None:
        if key not in self.memory_min:
            ele = [1, key]
            ith_min, ith_max = self.heap.insert(ele)
            self.memory_min[key] = ith_min
            self.memory_max[key] = ith_max
        else:
            ith_min = self.memory_min[key]
            ith_max = self.memory_max[key]
            index_min = self.heap.update(ith_min, 'min', 1)
            index_max = self.heap.update(ith_max, 'max', 1)
            self.memory_min[key] = index_min
            self.memory_max[key] = index_max


    def dec(self, key: str) -> None:
        ith_min = self.memory_min[key]
        ith_max = self.memory_max[key]
        index_min = self.heap.update(ith_min, 'min', -1)
        index_max = self.heap.update(ith_max, 'max', -1)
        self.memory_min[key] = index_min
        if self.heap.memory_min[index_min][0] == 0:
            self.heap.delete(index_min)
        self.memory_max[key] = index_max


    def getMaxKey(self) -> str:
        pass


    def getMinKey(self) -> str:
        pass