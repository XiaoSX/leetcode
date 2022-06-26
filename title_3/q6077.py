#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/22
'''

from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MODE = 1000000007
        n = len(strength)
        ans = 0
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                arr = strength[j:j + i]
                ans += (min(arr) % MODE ) * (sum(arr) % MODE) % MODE
                ans %= MODE
        return ans



if __name__ == '__main__':
    s = Solution()
    strength = [5, 4, 6]
    ans = s.totalStrength(strength)
    assert ans == 213
    strength = [1, 3, 1, 2]
    ans = s.totalStrength(strength)
    assert ans == 44