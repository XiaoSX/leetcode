#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/24
'''

class Solution:
    def binaryGap(self, n: int) -> int:
        max_v = 0
        update_cnt = 0
        cnt = 0
        while n:
            if n % 2 == 0:
                cnt += 1
            else:
                if update_cnt != 0:
                    max_v = max(max_v, cnt + 1)
                else:
                    update_cnt += 1
                cnt = 0
            n = n // 2

        return max_v


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    test.append(0)
    ans.append(0)
    test.append(8)
    ans.append(0)
    test.append(10)
    test.append(9)
    test.append(1)
    ans.append(2)
    ans.append(3)
    ans.append(0)
    for i in range(len(test)):
        assert s.binaryGap(test[i]) == ans[i]