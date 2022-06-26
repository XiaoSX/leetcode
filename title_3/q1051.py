#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/13
'''

# python list 传引用, 代码中会原地修改list, 但是递归会保存节点list,
# 递归退出的时候, list会被原来的值覆盖, 所有要有返回值才好
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    flag = arr[0]
    low = 0
    high = len(arr) - 1
    while low <= high:
        while low <= high and arr[low] <= flag:
            low += 1
        while low <= high and arr[high] >= flag:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    # high 所指元素一定比flag小, 且high一定有效, high不会到-1
    arr[0], arr[high] = arr[high], arr[0]
    arr[:high] = quick_sort(arr[:high])
    arr[high+1:] = quick_sort(arr[high+1:])
    return arr





from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect = quick_sort(heights[:])
        cnt = 0
        for i in range(len(expect)):
            if expect[i] != heights[i]:
                cnt += 1

        return cnt


if __name__ == '__main__':
    s = Solution()
    arr = [1, 0, 1, 0, 0, 0, 1, 2, 0, 0]
    quick_sort(arr)
    print(arr)