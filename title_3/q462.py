#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/19
'''

from typing import List
# 平方和最小, 会让大家的d尽量差不多, 所以会向均值靠近, 平方和最小 != 距离和最小
# d1 = [2, 3, 5]； d2 = [0, 1, 7]; d1 平方和最小, d2 距离和最小
# 距离和最小的是中位数
# 平方和最小的是均值
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        middle = nums[n // 2]
        return int(sum(abs(middle - x) for x in nums))


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    arr = [1,0,0,8,6]
    test.append(arr)
    ans.append(14)
    nums = [1, 10, 2, 9]
    test.append(nums)
    ans.append(16)
    nums = [1, 2, 3]
    test.append(nums)
    ans.append(2)
    for i in range(len(test)):
        assert s.minMoves2(test[i]) == ans[i]