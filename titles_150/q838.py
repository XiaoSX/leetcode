#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/2/21
'''

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = ['.' for _ in range(n)]
        # first < second 恒成立
        first = -1  # 上次界限位置
        second = 0
        while second < n:
            if dominoes[second] == 'L':
                if first >= 0 and dominoes[first] == 'R':
                    p = first
                    q = second
                    while p <= q:
                        if p == q:
                            ans[p] = '.'
                        else:
                            ans[p] = 'R'
                            ans[q] = 'L'
                        p += 1
                        q -= 1
                else:
                    p = first + 1
                    q = second
                    while p <= q:
                        ans[p] = 'L'
                        p += 1
                first = second

            elif dominoes[second] == 'R':
                if first >= 0 and dominoes[first] == 'R':
                    p = first
                    q = second
                    while p <= q:
                        ans[p] = 'R'
                        p += 1
                first = second

            second += 1

        if first < n and dominoes[first] == 'R':
            p = first
            q = n
            while p < q:
                ans[p] = 'R'
                p += 1

        return ''.join(ans)

