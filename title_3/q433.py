#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/5/7
'''

from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def distance(w0, w1):
            cnt = 0
            for i in range(8):
                if w0[i] != w1[i]:
                    cnt += 1
            return 1 if cnt == 1 else 0

        bank.append(start)
        bank = list(set(bank))
        m = len(bank)
        graph = [[0 for _ in range(m)] for _ in range(m)]
        init = -1
        end_i = -1
        min_v = 20
        visit = [0 for _ in range(m)]
        for i in range(m):
            if bank[i] == start:
                init = i
            if bank[i] == end:
                end_i = i

            for j in range(i + 1, m):
                wi = bank[i]
                wj = bank[j]
                graph[i][j] = distance(wi, wj)
                graph[j][i] = graph[i][j]

        def dfs(s, t, step):
            nonlocal min_v
            if s == t:
                min_v = min(min_v, step)
                return

            for i in range(m):
                if visit[i] == 0 and graph[s][i] == 1:
                    visit[i] = 1
                    dfs(i, t, step + 1)
                    visit[i] = 0

        visit[init] = 1
        dfs(init, end_i, 0)
        return -1 if min_v == 20 else min_v




if __name__ == '__main__':
    s = Solution()
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    test = []
    test.append([start, end, bank])
    ans = [1]

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    test.append([start, end, bank])
    ans.append(2)

    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    test.append([start, end, bank])
    ans.append(3)

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]
    test.append([start, end, bank])
    ans.append(4)

    for i in range(len(test)):
        assert s.minMutation(*test[i]) == ans[i]