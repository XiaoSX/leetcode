#  -*-  coding: utf-8  -*-

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)

        if not type(obstacleGrid[0]) == list:
            if sum(obstacleGrid) == 0:
                return 1
            else:
                return 0

        n = len(obstacleGrid[0])

        d = [[0 for _ in range(n)] for _ in range(m)]
        # init
        # 因为有障碍物，init不同
        for i in range(m-1, -1, -1):
            if obstacleGrid[i][n - 1] == 1:
                break
            d[i][n - 1] = 1
        for i in range(n-1, -1, -1):
            if obstacleGrid[m - 1][i] == 1:
                break
            d[m - 1][i] = 1

        i = m - 2
        while i >= 0:
            j = n - 2
            while j >= 0:
                # 障碍物不更新=0
                if obstacleGrid[i][j] == 1:
                    j -= 1
                    continue
                d[i][j] = d[i + 1][j] + d[i][j + 1]
                j -= 1
            i -= 1
        return d[0][0]