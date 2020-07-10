#  -*-  coding: utf-8  -*-

def do_sort(arr, indexs):
    n = len(arr)
    if n <= 1:
        return arr, indexs

    flag = arr[0]
    low = 1
    high = n - 1
    while low <= high:
        while low <= high and arr[low] <= flag:
            low += 1
        while low <= high and arr[high] >= flag:
            high -= 1

        if low < high:
            tmp = arr[low]
            arr[low] = arr[high]
            arr[high] = tmp

            tmp = indexs[low]
            indexs[low] = indexs[high]
            indexs[high] = tmp


    arr[0] = arr[high]
    arr[high] = flag

    tmp = indexs[0]
    indexs[0] = indexs[high]
    indexs[high] = tmp

    arr[:high], indexs[:high] = do_sort(arr[:high], indexs[:high])
    arr[high + 1:], indexs[high + 1:] = do_sort(arr[high + 1:], indexs[high + 1:])

    return arr, indexs


class Solution:
    def twoSum(self, nums, target: int):
        indexs = [i for i in range(len(nums))]
        nums, indexs = do_sort(nums, indexs)
        low = 0
        high = len(nums) - 1
        while low < high:
            sums = nums[low] + nums[high]
            if sums == target:
                return [indexs[low], indexs[high]]
            elif sums > target:
                high -=1
            else:
                low += 1