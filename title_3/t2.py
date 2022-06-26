#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/4/16
'''

from typing import List
class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        options = []
        n = len(cookbooks)
        def search(m, target, ans):
            if m == n:
                options.append(list(ans))
                return

            c1, c2, c3, c4, c5 = target
            m1, m2, m3, m4, m5 = cookbooks[m]
            if c1 >= m1 and c2 >= m2 and c3 >= m3 and c4 >= m4 and c5 >= m5:
                search(m + 1, [c1 - m1, c2 - m2, c3 - m3, c4 - m4, c5- m5], ans + [m])
            search(m + 1, target, ans)

        search(0, materials, [])
        max_v = -1
        for i in range(len(options)):
            a = 0
            b = 0
            for j in options[i]:
                x, y = attribute[j]
                a += x
                b += y
            if b >= limit:
                max_v = max(max_v, a)

        return max_v


if __name__ == '__main__':
    s = Solution()
    test = []
    ans = []
    meterials = [3, 2, 4, 1, 2]
    cookbooks = [[1, 1, 0, 1, 2], [2, 1, 4, 0, 0], [3, 2, 4, 1, 0]]
    attribute = [[3, 2], [2, 4], [7, 6]]
    limit = 5
    test.append([meterials, cookbooks, attribute, limit])
    ans.append(7)

    meterials = [10, 10, 10, 10, 10]
    cookbooks = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [10, 10, 10, 10, 10]]
    attribute = [[5, 5], [6, 6], [10, 10]]
    limit = 1
    test.append([meterials, cookbooks, attribute, limit])
    ans.append(11)


    for i in range(len(test)):
        assert s.perfectMenu(*test[i]) == ans[i]
