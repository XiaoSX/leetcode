#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/8
'''

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            if nums[i] == -1 or nums[i] == i + 1:
                i += 1
            else:
                j = nums[i] - 1
                if nums[i] == nums[j]:
                    ans.append(nums[i])
                    nums[i] = -1
                    i += 1
                    continue
                nums[i], nums[j] = nums[j], nums[i]

        return ans


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    test.append(nums)
    ans.append([2, 3])
    nums = [1, 1, 2]
    test.append(nums)
    ans.append([1])
    nums = [1]
    test.append(nums)
    ans.append([])
    for i in range(len(test)):
        assert set(s.findDuplicates(test[i])) == set(ans[i])