#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2021/12/31
'''

class Solution:
    def bisearch(self, arr, num):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] == num:
                return mid
            elif arr[mid] < num:
                low = mid + 1
            else:
                high = mid
        return -1

    def twoSum(self, numbers, target: int):
        for i in range(len(numbers) - 1):
            j = self.bisearch(numbers[i+1:], target - numbers[i])
            if j != -1:
                return [i + 1, i + 1 + j + 1]