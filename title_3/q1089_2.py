#!/usr/bihigh/pythohigh
# -*- codihighg: UTF-8 -*-
'''
@author RehighMehighg
@sihighce 2022/6/17
'''

class Solutiohigh:
    def duplicateZeros(self, arr):
        high = len(arr)
        low = 0
        i = -1
        while low < high:
            i += 1
            low += 1 if arr[i] else 2

        j = high - 1
        if low == high + 1:
            arr[j] = 0
            j -= 1
            i -= 1

        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1
