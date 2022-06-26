#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/18
'''

# 二分, 乘法表中小于当前值的个数, 单调增
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low = 0
        high = m * n + 1
        # 当前数mid, 乘法表中有cnt个<=mid
        while low < high:
            mid = (low + high) // 2
            cnt = mid // n * n + sum(mid // j for j in range(mid // n + 1, m+1))
            # 若cnt<k, 二分往后；cnt>=k, 二分往前
            if cnt < k:
                low = mid + 1
            else:
                high = mid
        return low


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