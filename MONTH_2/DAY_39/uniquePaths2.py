from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for y in range(m)] for x in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for y in range(n):
            for x in range(m):
                if obstacleGrid[y][x] == 1: continue
                if x > 0 and obstacleGrid[y][x-1] == 0: dp[y][x] += dp[y][x-1]
                if y > 0 and obstacleGrid[y-1][x] == 0: dp[y][x] += dp[y-1][x]
        return dp[-1][-1]