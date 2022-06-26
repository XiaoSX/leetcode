#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/6/3
'''

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        cnt = 0
        k = 1
        while n > (k * k + k) / 2:
            x = n / (k + 1) - k / 2
            if x - int(x) == 0:
                cnt += 1
            k += 1

        return cnt + 1


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append(15)
    ans.append(4)
    test.append(5)
    ans.append(2)
    test.append(9)
    ans.append(3)
    test.append(1)
    ans.append(1)
    test.append(2)
    ans.append(1)
    for i in range(len(test)):
        assert s.consecutiveNumbersSum(test[i]) == ans[i]