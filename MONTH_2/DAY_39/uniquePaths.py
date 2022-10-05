class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for y in range(m)] for x in range(n)]
        dp[0][0] = 1
        for y in range(n):
            for x in range(m):
                if x > 0: dp[y][x] += dp[y][x-1]
                if y > 0: dp[y][x] += dp[y-1][x]
        return dp[-1][-1]