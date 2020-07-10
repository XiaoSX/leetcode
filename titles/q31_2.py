#  -*-  coding: utf-8  -*-
class Solution:
    def nextPermutation(self, nums) -> None:
        n = len(nums)
        next_v = nums[n - 1]
        low = 0
        high = n - 1
        for i in range(n-2, -1, -1):
            if nums[i] >= next_v:
                next_v = nums[i]
            else:
                j = n - 1
                while j > i:
                    if nums[j] > nums[i]:
                        break
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                low = i + 1
                break

        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1


