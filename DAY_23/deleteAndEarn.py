from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = list(Counter(nums).items())
        nums.sort()
        prev = 0
        curr = nums[0][0]*nums[0][1]
        for x in range(1, len(nums)):
            new = nums[x][0]*nums[x][1]

            if nums[x-1][0] == nums[x][0] - 1:
                prev, curr = curr, max(prev+new, curr)
            else:
                prev, curr = curr, max(prev+new, curr+new)

        return curr

sol = Solution()

nums = [2,2,3,3,3,4]
print(sol.deleteAndEarn(nums))