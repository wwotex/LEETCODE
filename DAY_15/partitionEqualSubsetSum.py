from collections import Counter
import numpy as np

class Solution:
    def canPartition(self, nums) -> bool:
        S = sum(nums)
        if S % 2 != 0 or len(nums) == 1: return False
        S //= 2
        dp = [[False for x in range(S+1)] for y in range(len(nums)+1)]
        dp[0][0] = True
        for x in range(len(nums)+1):
            for y in range(S+1):
                if dp[x-1][y] or (y - nums[x-1] >= 0 and dp[x-1][y - nums[x-1]]): 
                    dp[x][y] = True
        
        return dp[-1][-1]

sol = Solution()
nums = [1,2,3,6]
print(sol.canPartition(nums))