#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/20
'''

from typing import List

def bi_search(num, arr):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid][0] < num:
            low = mid + 1
        else:
            high = mid
    return arr[low][1] if low < len(arr) else -1



class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = [(intervals[i][0], i) for i in range(len(intervals))]
        end = [(intervals[i][1], i) for i in range(len(intervals))]
        start = sorted(start, key=lambda x: x[0])
        end = sorted(end, key=lambda x: x[0])
        n = len(end)
        ans = [-1 for _ in range(n)]

        j = 0
        for p in end:
            while j < n and start[j][0] < p[0]:
                j += 1

            if j < n:
                ans[p[1]] = start[j][1]
        return ans


if __name__  == '__main__':
    s = Solution()
    test = []
    ans = []
    intervals = [[1, 4], [2, 3], [3, 4]]
    test.append(intervals)
    ans.append([-1, 2, -1])

    intervals = [[3, 4], [2, 3], [1, 2]]
    ans.append([-1, 0, 1])
    test.append(intervals)

    intervals = [[1, 2]]
    ans.append([-1])
    test.append(intervals)

    for i in range(len(test)):
        assert s.findRightInterval(test[i]) == ans[i]
