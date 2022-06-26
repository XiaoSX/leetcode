#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/5
'''

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        tmp = 1
        pri = 0
        for i in range(len(nums)):
            cur = nums[i]
            while tmp * cur >= k and pri < i:
                ans += i - pri
                tmp /= nums[pri]
                pri += 1

            if pri == i and tmp * cur >= k:
                tmp = 1
                pri += 1
            else:
                tmp *= cur

        while pri < len(nums):
            ans += len(nums) - pri
            tmp /= nums[pri]
            pri += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    nums = [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22]
    k = 18
    test.append([nums, k])
    ans.append(1)

    nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
    k = 19
    test.append([nums, k])
    ans.append(18)

    nums = [10, 5, 2, 6]
    k = 100
    test.append([nums, k])
    ans.append(8)

    nums = [1, 2, 3]
    k = 0
    test.append([nums, k])
    ans.append(0)

    for i in range(len(test)):
        assert s.numSubarrayProductLessThanK(*test[i]) == ans[i]
