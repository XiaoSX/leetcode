#  -*-  coding: utf-8  -*-

#  -*-  coding: utf-8  -*-
import copy

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    flag = arr[0]
    n = len(arr)
    low = 1
    high = n - 1
    while low <= high:
        while low < n and arr[low] <= flag:
            low += 1
        while high > 0 and arr[high] >= flag:
            high -= 1
        if low < high:
            tmp = arr[low]
            arr[low] = arr[high]
            arr[high] = tmp
    arr[0] = arr[high]
    arr[high] = flag
    arr[:high] = quick_sort(arr[:high])
    arr[high+1:] = quick_sort(arr[high+1:])
    return arr

def deep_search(arr, total, ans, final_ans):
    # 其他分支不搜索，直接回退

    if total == 0:
        final_ans.append(ans[:])
        return 1
    if len(arr) == 0:
        return 2

    used = []
    for i in range(len(arr)):
        if total - arr[i] < 0:
            break

        if arr[i] in used:
            continue
        ans.append(arr[i])
        used.append(arr[i])
        res = deep_search(arr[i+1:], total - arr[i], ans, final_ans)
        ans.pop()
        if res == 1:
            break
    return 2



class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates = quick_sort(candidates)
        ans = []
        final_ans = []

        deep_search(candidates, target, ans, final_ans)
        return final_ans