#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/27
'''

from typing import List
class Solution:

    def dfs(self, nums, equation, max_flag):
        if len(nums) == 0:
            return 1, ''

        if len(nums) == 1:
            return nums[0], str(equation[0])

        if len(nums) == 2:
            return nums[0] / nums[1], '{}/{}'.format(equation[0],  equation[1])

        ans1 = nums[0] / nums[1]
        result1 = '{}/{}'.format(equation[0],  equation[1])
        ans1, result1 = self.dfs([ans1] + nums[2:], [result1] + equation[2:], max_flag)

        sub_ans, sub_string = self.dfs(nums[1:], equation[1:], not max_flag)
        ans2 = nums[0] / sub_ans
        result2 = '{}/({})'.format(equation[0], sub_string)
        if max_flag:
            if ans1 >= ans2:
                return ans1, result1
            else:
                return ans2, result2
        else:
            if ans1 <= ans2:
                return ans1, result1
            else:
                return ans2, result2

    def optimalDivision(self, nums: List[int]) -> str:
        equation = [str(num) for num in nums]
        sub_ans, sub_str = self.dfs(nums, equation, True)
        # print(sub_ans)
        return sub_str
