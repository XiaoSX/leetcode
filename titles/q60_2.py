#  -*-  coding: utf-8  -*-
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        totals = [1]
        num = ['1']

        for i in range(1, n):
            totals.append(totals[i - 1] * i)
            num.append(str(i + 1))

        k -= 1
        ans = []
        for i in range(n - 1, -1, -1):
            ith = k // totals[i]
            k -= ith * totals[i]
            ans.append(num[ith])
            num.pop(ith)

        return ''.join(ans)