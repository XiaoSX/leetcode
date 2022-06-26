#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/28
'''

from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j - 1] % 2 != 0:
                j -= 1
            if i < j:
                nums[i], nums[j - 1] = nums[j - 1], nums[i]

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([1, 2, 3, 4]))