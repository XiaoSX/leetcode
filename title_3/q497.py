#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/9
'''

from typing import List
import random


def binary_search(arr, target):
    """
    bi_search target in the sorted arr
    返回最左边应该插入的index
    :param arr:
    :param target:
    :return:
    """
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.point_cnts = []
        cnt = 0
        for rect in rects:
            lb_x, lb_y, rt_x, rt_y = rect
            cnt += (rt_x - lb_x + 1) * (rt_y - lb_y + 1)
            self.point_cnts.append(cnt)



    def pick(self) -> List[int]:
        p_id = random.randint(1, self.point_cnts[-1])
        r_id = binary_search(self.point_cnts, p_id)
        lb_x, lb_y, rt_x, rt_y = self.rects[r_id]
        return [random.randint(lb_x, rt_x), random.randint(lb_y, rt_y)]


if __name__ == '__main__':
    rects = [[35330199, -46858448, 35330694, -46856950]]
    s = Solution(rects)
    print(s.pick())
