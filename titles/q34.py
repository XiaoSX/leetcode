#  -*-  coding: utf-8  -*-
# 递归的思路，注意返回值,什么时候下标相等，什么时候返回不相等下标
def bi_search(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    if len(nums) == 1:
        if target == nums[0]:
            return [0, 0]
        else:
            return [-1, -1]

    n = len(nums)
    low_i = 0
    high_i = n - 1
    mid_i = (low_i + high_i) // 2

    if nums[mid_i] > target:
        ans = bi_search(nums[:mid_i], target)

    elif nums[mid_i] < target:

        ans = bi_search(nums[mid_i + 1:], target)
        if ans != [-1, -1]:
            ans = [x + mid_i + 1 for x in ans]
    else:
        ans = bi_search(nums[:mid_i], target)
        if ans != [-1, -1]:
            low_i = ans[0]
        else:
            low_i = mid_i
        ans = bi_search(nums[mid_i + 1:], target)
        if ans != [-1, -1]:
            high_i = ans[-1] + mid_i + 1
        else:
            high_i = mid_i
        ans = [low_i, high_i]
    return ans

def normal(nums, target, left):
    low_i = 0
    high_i = len(nums)

    # low_i 去找high_i，说明mid<target,这种情况的结束条件一定是low_i == high_i
    #low_i 不会超过high_i, 结束需要mid==high_i,不可能（因为初始条件下low_i<high_i,一定成立，
    # 而且low_i == high_i会结束循环）
    # high_i 去找low_i，mid>=target，结束条件仍然low_i == high_i
    while low_i < high_i:
        mid_i = (low_i + high_i) // 2
        if nums[mid_i] > target or (left and nums[mid_i] == target):
            high_i = mid_i
        else:
            low_i = mid_i + 1
    return high_i


class Solution:
    def searchRange(self, nums, target: int):
        left_index = normal(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        else:
            return [left_index, normal(nums, target, False) - 1]