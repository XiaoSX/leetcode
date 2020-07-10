#  -*-  coding: utf-8  -*-
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dis = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            dis[i][0] = i
        for i in range(1, n + 1):
            dis[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dis[i][j] = dis[i - 1][j - 1]
                else:
                    # replace, insert, delete
                    dis[i][j] = min(dis[i - 1][j - 1], dis[i][j - 1], dis[i - 1][j]) + 1
        return dis[m][n]