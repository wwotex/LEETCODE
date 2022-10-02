class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for y in range(target+1)] for x in range(n+1)]
        dp[0][0] = 1
        for throw in range(1, n+1):
            for sum in range(1, target+1):
                for prev_sum in range(sum):
                    if sum - prev_sum <= k:
                        dp[throw][sum] = (dp[throw][sum] + dp[throw-1][prev_sum]) % 1000000007
        return dp[-1][-1]

sol = Solution()
n = 30
k = 30
target = 500
print(sol.numRollsToTarget(n, k, target))