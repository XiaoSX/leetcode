#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-02
'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    low = 0
    high = len(arr) - 1
    while low <= high:
        while low <= high and arr[low] <= pivot:
            low += 1
        while low <= high and arr[high] > pivot:
            high -= 1
        if low < high:
            tmp = arr[low]
            arr[low] = arr[high]
            arr[high] = tmp
    arr[0] = arr[low - 1]
    arr[low - 1] = pivot
    arr[:low - 1] = quicksort(arr[:low - 1])
    arr[low:] = quicksort(arr[low:])
    return arr

class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = quicksort(nums)
        if len(nums) <= 0:
            return 0
        pre_p = nums[0]
        max_len = 1
        length = 1
        # 循环结束后的条件判断很容易忘记
        # 初始化的时候, 长度为1, 算上自己
        for p in nums[1:]:
            if p == pre_p:
                continue
            if p - 1 == pre_p:
                length += 1
            else:
                max_len = max(max_len, length)
                length = 1
            pre_p = p
        return max(max_len, length)