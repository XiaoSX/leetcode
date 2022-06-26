#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/5
'''
import string
# '?' 可以出现在任意位置
# 非'?' 可以出现在任意'?'位置


def is_plex(s):
    if len(s) == 1:
        return False

    if s[-1] == s[-2]:
        return True

    n = len(s)
    for i in range(1, n // 2 + 1):
        if s[-i:] == s[-2 * i:-i]:
            return True
    return False



class Solution:
    def modifyString(self, s: str):
        order_map = {}
        m = len(s)
        for i in range(len(s)):
            t = s[i]
            if t not in order_map:
                order_map[t] = [i]
            else:
                order_map[t].append(i)

        dp = [[[] for _ in range(101)] for _ in range(101)]
        for i in range(len(s)):
            if s[i] != '?':
                points = list(set(order_map[s[i]] + order_map['?']))
                dp[i][1] = [x for x in points if x < i]
            else:
                dp[i][1] = [x for x in range(i - 1)]

        for i in range(1, len(s)):
            cur_points = dp[i][1]
            for j in range(2, 100):
                if len(dp[i - 1][j - 1]) == 0:
                    break

                dp[i][j] = list(set([x-j+1 for x in cur_points if x - j >= -1]).union(set(dp[i-1][j-1])))
                dp[i][j] = [p for p in dp[i][j] if i - p + 1 >= 2 * j]

                if len(dp[i][j]) == 0:
                    break

        ans = {}
        for i in range(m):
            for j in range(1, 101):
                if len(dp[i][j]) == 0:
                    break

                for p in dp[i][j]:
                    if i - 2 * j + 1 == p:
                        fi = p
                        fj = p + j
                        high = fj
                        while fi < high:
                            if s[fi] == '?':
                                if fi not in ans:
                                    ans[fi] = set()
                                ans[fi].add(s[fj])
                            fi += 1
                            fj += 1
        new_s = []
        for i in range(m):
            if s[i] != '?':
                new_s.append(s[i])
            else:
                for j in string.ascii_lowercase:
                    if i not in ans or j not in ans[i]:
                        new_s.append(j)
                        if is_plex(new_s[:i+1]):
                            new_s = new_s[:-1]
                            continue
                        break

        return ''.join(new_s)