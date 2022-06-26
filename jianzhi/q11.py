#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/9
'''

from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        m = len(numbers)
        low = 0
        high = m
        while low < high:
            mid = (low + high) // 2
            if numbers[mid] == numbers[low]:
                low += 1
            elif numbers[mid] < numbers[low]:
                if high == mid + 1:
                    return numbers[mid]
                high = mid + 1
            else:
                if numbers[high - 1] <= numbers[low]:
                    low = mid + 1
                else:
                    return numbers[low]
        return numbers[low - 1]


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    numbers = [2, 1]
    test.append(numbers)
    ans.append(1)
    test.append([1])
    ans.append(1)
    test.append([1, 2, 3])
    ans.append(1)
    test.append([1, 1])
    ans.append(1)
    test.append([1, 2])
    ans.append(1)
    for i in range(len(test)):
        print(i)
        assert s.minArray(test[i]) == ans[i]