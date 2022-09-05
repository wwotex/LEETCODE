from collections import Counter

class Solution:
    def canPartition(self, nums) -> bool:
        S = sum(nums)
        if S % 2 != 0 or len(nums) == 1: return False
        S //= 2
        dp = [{} for x in range(S+1)]
        dp[0] = Counter(nums)
        for x in range(1,S+1):
            for num in nums:
                if x-num >= 0 and num in dp[x-num]:
                    dp[x] = dp[x-num].copy()
                    dp[x][num] -= 1 
                    if dp[x][num] <= 0: dp[x].pop(num)
        return bool(dp[S])



sol = Solution()
nums = [7,36,41,74,96,24,73,65,15,47,75,92,68,25,58,11,26,55,5,16,96,92,47,96,24,42,20,92,92,1,72,20,54,2,18,80,50,37,13,11,23,80,82,72,55,95,56,91,39,90,83,91,44,41,18,48,96,97,45,4,70,36,40,27,34,25,38,27,7,80,69,87,30,99,72,96,64,59,72,74,15,66,80,63,33,28,50,26,54,46,3,81,48,84,97,85,51,41,14,19]
print(sol.canPartition(nums))