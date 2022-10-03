class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for x in range(max(n+1, 2))]
        dp[0], dp[1] = 1, 1
        for tot in range(2, n+1):
            for k in range(tot):
                dp[tot] += dp[k]*dp[tot-k-1]
        return dp[n]

sol = Solution()
n = 4
print(sol.numTrees(n))
