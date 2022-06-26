#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-12-11
'''

import numpy as np
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        if m == 0:
            return 1
        if isinstance(dungeon[0], int):
            ans = [float('inf') for _ in range(m + 1)]
            for i in range(m - 1, -1, -1):
                ans[i] = min(ans[i], max(1, ans[i + 1] - dungeon[i]))
            return ans[0]

        n = len(dungeon[0])
        ans = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        ans[m-1][n-1] = max(1, 1-dungeon[m-1][n-1])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                ans[i][j] = min(max(1, ans[i + 1][j] - dungeon[i][j]),
                                max(1, ans[i][j + 1] - dungeon[i][j]),
                                ans[i][j])
        return ans[0][0]
