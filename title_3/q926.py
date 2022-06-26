#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/11
'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero_count = []
        one_count = []

        n = len(s)
        low = 0
        high = len(s) - 1
        while low < n and s[low] == '0':
            low += 1

        while high >= 0 and s[high] == '1':
            high -= 1

        if low > high:
            return 0

        while low < high + 1:
            i = low
            while i < high + 1 and s[i] == s[low]:
                i += 1
            if s[low] == '0':
                zero_count.append(i - low)
            else:
                one_count.append(i - low)
            low = i

        n = len(zero_count)
        f_full_zero = one_count[0]
        f_full_one = zero_count[0]
        f_zero_one = one_count[0] + zero_count[0]
        for i in range(1, n):
            f_zero_one = min(f_full_zero + zero_count[i], f_zero_one + zero_count[i])
            f_full_zero += one_count[i]
            f_full_one += zero_count[i]

        return min(f_zero_one, f_full_zero, f_full_one)


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    t = "00110"
    test.append(t)
    ans.append(1)
    t = "010110"
    test.append(t)
    ans.append(2)
    t = "00011000"
    test.append(t)
    ans.append(2)

    t = '11111'
    test.append(t)
    ans.append(0)

    t = '00000'
    test.append(t)
    ans.append(0)
    for i in range(len(test)):
        assert s.minFlipsMonoIncr(test[i]) == ans[i]
