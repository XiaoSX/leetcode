#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/10
'''

from typing import List
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        i = len(nums) - 2
        while k > 0:
            if i < 0:
                pre_v = float('inf')
            else:
                pre_v = nums[i]
            cur = nums[i + 1]
            if k >= (len(nums) - i - 1) * (pre_v - cur):
                for j in range(i+1, len(nums)):
                    nums[j] += pre_v - cur
                    k -= pre_v - cur
                i -= 1
            else:
                cnt = len(nums) - i - 1
                amount = k // cnt
                remain = k % cnt
                for j in range(i + 1, len(nums)):
                    nums[j] += amount
                    k -= amount
                    while remain > 0:
                        remain -= 1
                        nums[j] += 1
                        k -= 1
                break


        ans = 1
        for i in range(len(nums)):
            ans *= nums[i] % 1000000007
        ans %= 1000000007
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [0, 4]
    k = 5
    ans = s.maximumProduct(nums, k)
    print(ans % 1000000007)