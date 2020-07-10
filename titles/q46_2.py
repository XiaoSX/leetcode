#  -*-  coding: utf-8  -*-

# 数组交换后,自然形成一种排列
def do_permute(first, n, ans, arr):
    if first == n:
        ans.append(arr[:])

    for i in range(first, n):
        arr[i], arr[first] = arr[first], arr[i]
        do_permute(first + 1, n, ans, arr)
        arr[i], arr[first] = arr[first], arr[i]



class Solution:
    def permute(self, nums):
        ans = []
        do_permute(0, len(nums), ans, nums)
        return ans