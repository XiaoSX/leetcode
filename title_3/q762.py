#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/5
'''


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        def combine(n, m):
            ans = 1
            for i in range(m + 1, n + 1):
                ans *= i
            for i in range(1, n -m +1):
                ans //= i
            return ans

        def leNum(num):
            ans = []
            while num:
                ans.append(num % 2)
                num = num // 2

            cnt = 0
            n = len(ans)
            pri = 0
            for i in range(n - 1, -1, -1):
                if ans[i] == 1:
                    if i == 0 and pri in factors:
                        cnt += 1
                        continue

                    for j in factors:
                        if j - pri < 0:
                            continue

                        if j - pri > i:
                            break
                        cnt += combine(i, j - pri)
                    pri += 1
            return cnt

        a = leNum(left)
        b = leNum(right)
        ans = []

        while right:
            ans.append(right % 2)
            right = right // 2
        if sum(ans) in factors:
            return b - a + 1
        else:
            return b - a


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append([6, 10])
    ans.append(4)

    test.append([10, 15])
    ans.append(5)

    test.append([1, 2])
    ans.append(0)

    test.append([2, 3])
    ans.append(1)
    for i in range(len(test)):
        assert s.countPrimeSetBits(*test[i]) == ans[i]

