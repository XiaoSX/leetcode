#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/16
'''

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        cnt = 0
        i = 0
        pre = None

        for j in range(len(nums)):
            if nums[j] == pre:
                continue

            while nums[j] - nums[i] > k:
                i += 1
            if nums[j] - nums[i] == k and j != i:
                pre = nums[j]
                cnt += 1

        return cnt

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    # nums = [3, 1, 4, 1, 5]
    # k = 2
    # test.append([nums, k])
    # ans.append(2)
    #
    # nums = [1, 2, 3, 4, 5]
    # k = 1
    # test.append([nums, k])
    # ans.append(4)

    nums = [1, 3, 1, 3, 5, 4, 4, 1, 4]
    k = 0
    test.append([nums, k])
    ans.append(3)

    for i in range(len(test)):
        assert s.findPairs(*test[i]) == ans[i]