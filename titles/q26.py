#  -*-  coding: utf-8  -*-
class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0

        pre_v = -1
        pre_i = -1
        for i in range(n):
            if i == 0:
                pre_i = i
                pre_v = nums[i]
                continue
            if nums[i] == pre_v:
                continue

            if pre_i + 1 != i:
                nums[pre_i + 1] = nums[i]
            pre_v = nums[i]
            pre_i += 1

        return pre_i + 1