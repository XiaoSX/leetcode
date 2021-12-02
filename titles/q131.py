#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@version 1.0
@since 2021-06-10
'''
# 递归结束total_ans.append的是list的copy, if not, list会被更新
def dfs(g, visit, ans, new_s, total_ans):
    n = len(g[0])
    if visit == n:
        total_ans.append(list(ans))
        return

    for i in range(n):
        if g[visit][i] == 1:
            ans.append(new_s[visit:i+1])
            dfs(g, i + 1, ans, new_s, total_ans)
            ans.pop(-1)

# 坑人的下标
class Solution:
    def partition(self, s: str):
        n = len(s)
        new_s = '#'.join(list(s))
        d = [[0 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
        ans = []
        l = 1
        # 遍历的未位下标是n - l,此处(2n - 1 - l)
        for i in range(0, 2 * n - l):
            d[i][i] = 1

        # 句子长度从3开始
        for l in range(2, 2 * n - 1, 2):
            for i in range(0, 2 * n - 1 - l):
                if d[i + 1][i + l - 1] == 1 and new_s[i] == new_s[i + l]:
                    d[i][i + l] = 1
                else:
                    d[i][i + l] = 0


        new_d = [[d[i][j] for j in range(0, 2 * n - 1, 2)] for i in range(0, 2 * n - 1, 2)]
        ans = []
        total_ans = []
        dfs(new_d, 0, ans, s, total_ans)
        return total_ans



