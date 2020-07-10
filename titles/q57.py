#  -*-  coding: utf-8  -*-
def bi_search(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid + 1
        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid

    return low


class Solution:
    def insert(self, intervals, newInterval):
        insert_i = bi_search([x[0] for x in intervals], newInterval[0])

        low = 0
        merged = []
        while low < insert_i:
            merged.append(intervals[low])
            low += 1
        if not merged or merged[-1][1] < newInterval[0]:
            merged.append(newInterval)
        else:
            merged[-1][1] = max(merged[-1][1], newInterval[1])

        while low < len(intervals):
            interval = intervals[low]
            if merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
            low += 1
        return merged