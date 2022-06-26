#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/5
'''

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    nums = [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22]
    k = 18
    test.append([nums, k])
    ans.append(1)

    for i in range(len(test)):
        assert s.numSubarrayProductLessThanK(*test[i]) == ans[i]

