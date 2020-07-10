#  -*-  coding: utf-8  -*-
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1

        return high