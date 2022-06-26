#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/15
'''

from typing import List

def bi_search(arr, target, low, high):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid

    return low

def count(arr, target):
    i = 0
    cnt = 0
    for j in range(len(arr)):
        while arr[j] - arr[i] > target:
            i += 1
        cnt += j - i
    return cnt


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return 0

        left = 0
        right = nums[-1] - nums[0] + 1
        # 最小的数对和 是0
        # 小于v的cnt对 的数对和 有多种情况
        while left < right:
            # 数对和 是mid
            mid = (left + right) // 2
            # cnt = 0
            # for i in range(n):
                # j = bi_search(nums, nums[i] + mid, i, n)
                # cnt += j - i - 1

            cnt = count(nums, mid)

            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    nums = [1, 3, 1]
    k = 1
    test.append([nums, k])
    ans.append(0)

    nums = [1, 1, 1]
    k = 2
    test.append([nums, k])
    ans.append(0)

    nums = [1, 6, 1]
    k = 3
    test.append([nums, k])
    ans.append(5)

    nums = [9, 10, 7, 10, 6, 1, 5, 4, 9, 8]
    k = 18
    test.append([nums, k])
    ans.append(2)

    for i in range(len(test)):
        print(s.smallestDistancePair(*test[i]))
        assert s.smallestDistancePair(*test[i]) == ans[i]