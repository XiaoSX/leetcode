#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/8
'''

from typing import List
from collections import defaultdict
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        turn_on = set()
        row_cnt = defaultdict(lambda :0)
        col_cnt = defaultdict(lambda :0)
        main_di_cnt = defaultdict(lambda :0)
        di_cnt = defaultdict(lambda :0)

        for i in range(len(lamps)):
            x, y = lamps[i]
            if (x, y) in turn_on:
                continue
            turn_on.add((x, y))
            row_cnt[x] += 1
            col_cnt[y] += 1
            main_di_cnt[x - y] += 1
            di_cnt[x + y] += 1

        ans = []
        for i in range(len(queries)):
            x, y = queries[i]
            if row_cnt[x] > 0 or col_cnt[y] > 0 or \
                    main_di_cnt[x - y] > 0 or di_cnt[x + y] > 0:
                ans.append(1)
            else:
                ans.append(0)
            areas = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 0), (0, 1),
                     (1, -1), (1, 0), (1, 1)]
            for jx, jy in areas:
                jx = x + jx
                jy = y + jy
                if (jx, jy) in turn_on:
                    turn_on.remove((jx, jy))
                    row_cnt[jx] -= 1
                    col_cnt[jy] -= 1
                    main_di_cnt[jx - jy] -= 1
                    di_cnt[jx + jy] -= 1

        return ans
