#  -*-  coding: utf-8  -*-
class Solution:
    def reverse(self, x: int) -> int:
        min_INF = -2147483648
        max_INF = 2147483647

        sign = -1 if x < 0 else 1

        ans = []
        x = abs(x)
        if x == 0:
            return x

        while x > 0:
            ans.append(x % 10)
            x = x // 10

        n = len(ans)
        total = 0
        tmp = 1
        for i in range(n - 1, -1, -1):
            total += ans[i] * tmp
            tmp *= 10

        if sign < 0:
            return 0 if -total < min_INF else -total
        else:
            return  0 if total > max_INF else total