#  -*-  coding: utf-8  -*-
class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n <= 2:
            return n
        cnt = 1
        pre_v = nums[0]
        cur_i = 1
        for i in range(1, n):
            if nums[i] == pre_v and cnt < 2:
                nums[cur_i] = nums[i]
                cnt += 1
                cur_i += 1
            elif nums[i] != pre_v:
                cnt = 1
                nums[cur_i] = nums[i]
                pre_v = nums[cur_i]
                cur_i += 1
            else:
                pass
        return cur_i