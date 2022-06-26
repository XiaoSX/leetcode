#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/18
'''


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        cols = [1 for _ in range(m)]

        while True:
            curs = [(i + 1) * cols[i] if cols[i] <= n else m * n + 1 for i in range(m)]
            min_row = 0
            for i in range(m):
                if curs[i] < curs[min_row]:
                    min_row = i
            if k == 1:
                return curs[min_row]
            cols[min_row] += 1
            k -= 1



if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append([1, 1, 1])
    ans.append(1)
    m = 3
    n = 3
    k = 5
    test.append([m, n, k])
    ans.append(3)
    m = 2
    n = 3
    k = 6
    test.append([m, n, k])
    ans.append(6)
    for i in range(len(test)):
        assert s.findKthNumber(*test[i]) == ans[i]