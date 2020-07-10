#  -*-  coding: utf-8  -*-
def combine(start, end, depth, arr, ans, final):
    if depth == 0:
        final.append(ans[:])

    used = []
    for i in range(start, end):
        if arr[i] not in used:
            used.append(arr[i])
            ans.append(arr[i])
            combine(i + 1, end, depth - 1, arr, ans, final)
            ans.pop(-1)

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        final = [[]]
        for k in range(1, n + 1):
            combine(0, n, k, nums, ans, final)
        return final