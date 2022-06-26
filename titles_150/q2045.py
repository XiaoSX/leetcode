#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/24
'''

from typing import List

class Solution:
    def dfs(self, n, paths, cnt):
        if n == 1 and cnt == 0:
            return True

        if cnt == 0:
            return False

        for i in paths[n]:
            if self.dfs(i, paths, cnt - 1):
                return True

        return False

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 广搜找最短路径
        # 最短路径变为两条路径 + 1(parents)
        # else +2
        paths = {}
        for e in edges:
            s, t = e
            if s not in paths:
                paths[s] = [t]
            else:
                paths[s].append(t)

            if t not in paths:
                paths[t] = [s]
            else:
                paths[t].append(s)

        visit = [0 for _ in range(n+1)]
        visit[1] = 1
        queue = [1]
        cnt = 0
        flag = False
        while len(queue) > 0:
            q_size = len(queue)
            for i in range(q_size):
                node = queue[i]
                if node == n:
                    flag = True
                    break
                for node_j in paths[node]:
                    if visit[node_j] == 0:
                        queue.append(node_j)
                        visit[node_j] = 1
            if flag:
                break
            queue = queue[q_size:]
            cnt += 1
        print('shortest path: ', cnt)

        if self.dfs(n, paths, cnt+1):
            last_p = cnt + 1
        else:
            last_p = cnt + 2

        # 到达目的地的时候不需要等红灯
        # 根本不需要等红灯
        if change >= time:
            street_n = change // time + (1 if change % time > 0 else 0)
            street_t = 2 * change
        else:
            street_n = 1
            while street_n <= last_p and street_n * time // change % 2 == 0:
                street_n += 1
            street_t = (street_n * time // change + 1) * change

        print('street_n {}, street_t {}, need_step {}'.format(street_n, street_t, last_p))
        total_t = 0
        while last_p > street_n:
            total_t += street_t
            last_p -= street_n
        total_t += last_p * time
        return total_t




