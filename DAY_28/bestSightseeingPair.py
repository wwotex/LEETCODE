from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        start = 0
        max_score = 0
        for i, el in enumerate(values[1:], 1):
            if values[i-1]-1 > values[start]-i+start:
                start = i-1
            max_score = max(max_score, (el+values[start]+start-i))
        return max_score

sol = Solution()
nums = [7,8,8,10]
print(sol.maxScoreSightseeingPair(nums))