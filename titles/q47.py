#  -*-  coding: utf-8  -*-
import copy

def quick_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    flag = nums[0]
    low_i = 0
    high_i = n - 1
    while low_i <= high_i and low_i < n and high_i > 0:
        while low_i < n and nums[low_i] <= flag:
            low_i += 1
        while high_i > 0 and nums[high_i] >= flag:
            high_i -= 1

        if low_i < high_i:
            tmp = nums[low_i]
            nums[low_i] = nums[high_i]
            nums[high_i] = tmp

    nums[0] = nums[high_i]
    nums[high_i] = flag
    nums[:high_i] = quick_sort(nums[:high_i])
    nums[high_i+1:] = quick_sort(nums[high_i + 1:])
    return nums


def deep_search(graph, visited, ans, total_ans):
    n = len(graph)
    used = []
    for i in range(n):
        if visited[i] == 1:
            continue

        if graph[i] in used:
            continue

        used.append(graph[i])

        visited[i] = 1
        ans.append(graph[i])
        deep_search(graph, visited, ans, total_ans)
        del ans[-1]
        visited[i] = 0
    if len(ans) == n:
        total_ans.append(copy.deepcopy(ans))




class Solution:
    def permuteUnique(self, nums):
        visited = [0 for _ in range(len(nums))]
        ans = []
        total_ans = []
        deep_search(nums, visited, ans, total_ans)
        return total_ans
