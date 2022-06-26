#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/17
'''

from typing import List
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        mem = {}
        for t in tasks:
            if t not in mem:
                mem[t] = 0
            mem[t] += 1

        for t in mem:
            cnt = mem[t]
            if cnt // 3 == 0 and cnt // 2 == 0:
                return -1
            if cnt // 3 == 0:
                ans += 1
            else:
                ans += cnt // 3
                if cnt % 3 != 0:
                    ans += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    test.append(tasks)
    ans.append(4)

    tasks = [2, 3, 3]
    test.append(tasks)
    ans.append(-1)
    for i in range(len(test)):
        assert s.minimumRounds(test[i]) == ans[i]


