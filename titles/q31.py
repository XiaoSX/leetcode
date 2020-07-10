#  -*-  coding: utf-8  -*-

# 局部最优的感觉

def maopao_sort(arr, low, high):
    for i in range(0, high - low - 1):
        j = low
        while j < high - 1 - i:
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
            j += 1


def reverse(arr, start):
    n = len(arr)
    j = n - 1
    while start < j:
        tmp = arr[start]
        arr[start] = arr[j]
        arr[j] = tmp
        start += 1
        j -= 1



class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        n = len(nums)
        j = n - 1
        pre = nums[j]
        while j >= 0 and nums[j] >= pre:
            pre = nums[j]
            j -= 1

        # 情况可以归一，j actually != n-1
        # 交换后，reverse j + 1

        # # 没有找到逆序
        # if j == n - 1:
        #     tmp = nums[j]
        #     nums[j] = nums[j - 1]
        #     nums[j - 1] = tmp
        #     return

        # 不需要单独考虑
        # 已经是最大
        if j == -1:
            return reverse(nums, 0)

        # 否则交换后升序
        for i in range(n-1, j, -1):
            if nums[i] > nums[j]:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                break
        reverse(nums, j + 1)

