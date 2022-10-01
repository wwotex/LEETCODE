class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for el in s]
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 1 <= int(s[i-1] + s[i]) <= 26 and s[i-1] != '0':
                dp[i] += dp[i-2] if i-2 >= 0 else 1

        return dp[-1]

sol = Solution()
s = '9'
print(sol.numDecodings(s))