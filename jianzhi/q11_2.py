#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/11
'''

from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        m = len(numbers)
        low = 0
        high = m
        while low < high:
            mid = (low + high) // 2
            if numbers[mid] > numbers[high - 1]:
                low = mid + 1
            elif numbers[mid] < numbers[high - 1]:
                high = mid + 1
            else:
                if high == mid + 1:
                    return min(numbers[mid], numbers[low])
                high -= 1
        return numbers[low - 1]


if __name__ == '__main__':
    s = Solution()
    num = [1]
    print(s.minArray(num))