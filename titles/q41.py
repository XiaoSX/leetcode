#  -*-  coding: utf-8  -*-
class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 1

        low_i = 0
        high_i = n - 1
        # 漏掉了重复value case
        # 不往前换[1, 1]
        # 调换的值same[2, 2]
        # 调换的位置same
        # nums[low_i] 已被更新，不能在做下标
        while low_i <= high_i:
            if nums[low_i] <= 0 or nums[low_i] - 1 > high_i or nums[low_i] - 1 < low_i:
                tmp = nums[low_i]
                nums[low_i] = nums[high_i]
                nums[high_i] = tmp
                high_i -=1
            elif low_i != nums[low_i] - 1:
                if nums[low_i] != nums[nums[low_i] - 1]:
                    tmp = nums[low_i]
                    nums[low_i] = nums[tmp - 1]
                    nums[tmp - 1] = tmp
                else:
                    nums[low_i] = -1
            elif low_i == nums[low_i] - 1:
                low_i += 1
        return low_i + 1
