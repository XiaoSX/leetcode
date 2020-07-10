#  -*-  coding: utf-8  -*-

class Solution:
    def removeElement(self, nums, val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        i = 0
        j = n - 1
        while i <= j:
            while i <= j and nums[j] == val:
                j -= 1
            while i <= j and nums[i] != val:
                i += 1

            if i < j:
                nums[i] = nums[j]
                i += 1
                j -= 1

        return i
