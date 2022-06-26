#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/3
'''

from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        l, r = 1, 10000001
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            for can in candies:
                cnt += can // mid
            if cnt >= k:
                l = mid + 1
            else:
                r = mid
        return l - 1


if __name__ == '__main__':
    test = []
    ans = []
    s = Solution()
    candies = [5, 8, 6]
    k = 3
    test.append([candies, k])
    ans.append(5)
    candies = [2, 5]
    k = 11
    test.append([candies, k])
    ans.append(0)

    candies = [1, 4, 9]
    k = 2
    test.append([candies, k])
    ans.append(4)

    candies = [1, 2, 9]
    k = 2
    test.append([candies, k])
    ans.append(4)

    candies = [4, 7, 5]
    k = 4
    test.append([candies, k])
    ans.append(3)

    candies = [1,2,6,8,6,7,3,5,2,5]
    k = 3
    test.append([candies, k])
    ans.append(6)

    for i in range(len(test)):
        assert s.maximumCandies(*test[i]) == ans[i]